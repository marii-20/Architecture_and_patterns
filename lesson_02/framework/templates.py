import os

from jinja2 import Template


def render_(template_name, folder='templates', **kwargs):
    """
    :param template_name: имя шаблона
    :param folder: папка в которой ищем шаблон
    :param kwargs: параметры
    :return:
    """
    file_path = os.path.join(folder, template_name)
    with open(file_path, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**kwargs)


if __name__ == '__main__':
    # Пример использования
    output_test = render_('index.html', name_company='ООО Сладкоежка')
    print(output_test)
