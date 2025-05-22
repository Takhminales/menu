# menuapp/templatetags/menu_tags.py
from django import template
from django.urls import NoReverseMatch
from menuapp.models import MenuItem  # Замените на ваше имя приложения

register = template.Library()

@register.inclusion_tag('menuapp/menu_draw.html', takes_context=True)
def draw_menu(context, menu_name):
    """
    Отображает древовидное меню по имени menu_name.
    Меню строится одним SQL-запросом и включает флаги активности и раскрытия.
    """
    request = context.get('request')
    current_path = request.path if request else ''

    # Загружаем все пункты меню с related menu__name
    menu_items = list(
        MenuItem.objects.filter(menu__name=menu_name)
        .select_related('parent', 'menu')
        .order_by('order')
    )
    if not menu_items:
        return {'menu_tree': [], 'request': request}

    # Словарь: id -> объект
    items_by_id = {item.id: item for item in menu_items}

    # Построение дерева: parent_id -> [дети]
    children_map = {}
    for item in menu_items:
        children_map.setdefault(item.parent_id, []).append(item)

    # Функция безопасного получения URL (через named url или прямой url)
    def get_url(item):
        try:
            return item.get_url()
        except NoReverseMatch:
            return item.url or '#'

    # Поиск активного элемента
    active_item = next((item for item in menu_items if get_url(item) == current_path), None)

    # Получение всех ID предков активного элемента
    def get_ancestor_ids(item):
        ids = set()
        while item:
            ids.add(item.id)
            item = items_by_id.get(item.parent_id)
        return ids

    expanded_ids = get_ancestor_ids(active_item) if active_item else set()

    # Рекурсивная сборка дерева
    def build_tree(parent_id=None):
        items = []
        for item in children_map.get(parent_id, []):
            is_active = active_item and item.id == active_item.id
            is_expanded = item.id in expanded_ids
            children = build_tree(item.id) if is_expanded or parent_id is None else []
            items.append({
                'item': item,
                'children': children,
                'active': is_active,
                'expanded': is_expanded,
            })
        return items

    return {
        'menu_tree': build_tree(),
        'request': request,
    }
