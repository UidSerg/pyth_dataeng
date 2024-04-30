# проверка функций из пакета созданного пакета по заданию 3

from file_edit import generate_name
from file_edit import rename_group

generate_name.generate_files('rnd', 'files')
rename_group.rename_group("New", 5, "txt", "doc", [0,3])