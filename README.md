Program: protopy
Version: 1
Creator: Ilya Solomein

# О программе
Эта программа включает в себя три модуля. 
protoc - консольная программа. Позволяет из proto файла создать python класс, который после будет 
использоваться при сериализации и десериализации данных. 

encoder позволяет сериализировать данные.

decoder позволяет десериализровать данные из строки. 


## Пример запуска protoc

Base dir = protopy 

Linux bash
```shell script
python3 protoc/protoc.py -h [--help] # выводит help
python3 protoc/protoc.py -p [--python_in] file.proto # получает на вход файл с расширением proto, который будет преобразован в file_gen.py
```

Windows cmd
```shell script
py protoc\protoc.py -h [--help]
py protoc\protoc.py -p [--python_in] file.proto 
```

## encoder: 
Пакет, в котором есть класс ProtoEncoder, который принимает на вход класс, который создан с ипользованием protoc и 
сериализует данные в этом классе в строку.

Пример использования: 

Допустим, с помощью protoc мы сгенерировали файл a_gen.py из файла a.proto с содержанием: 
```proto
syntax = "proto3";

message Book {
  string name = 1;
  int32 pages = 2;
}
```

Тогда encoder можно использовать так
```python
from encoder.ProtoEncoder import ProtoEncoder
from a_gen import Book # Класс сгенерированный protoc

generated_class = Book()
generated_class.name = "Some Name"
generated_class.pages = 200

encoder = ProtoEncoder(class_to_encode=generated_class)
result = encoder.encode_to_string()
print(result)
```

## decoder: 
Пакет, в котором есть класс ProtoDecoder, который принимает на вход класс, который создан с использованием protoc и 
заполняет этот класс десериализованными данными.

Пример использования:

```python
from decoder.ProtoDecoder import ProtoDecoder
from a_gen import Book

instance_class = Book()

decoder = ProtoDecoder(instance_class=instance_class)

decoder.decode_from_string(b'\n\tSome Name\x10\x00\x00\x00\xc8') # сериализованные данные из прошлого примера

print(instance_class.pages) # напечатает 200
print(instance_class.name) # напечатает "Some Name"
```

## Что может эта версия: 
Сериализациия и десериализация целых типов неограниченной длины. 
Сериализациия и десериализация строк.
Сериализациия и десериализация булевых значений. 
Сериализованные этой программой данные совместимы с гугловским protobuf. 

Что не может эта версия:
protoc не может во вложенность, импорт, enum. 
Нет возможности работать с числами с плавающей точкой. 

Version: 2

Что изменилось:
Добавлены: enum (вложенные и нет), сериализация чисел с плавающей точкой, словари, отрицательные целочисленные, тесты
Совместимость с оригинальным protobuf перестала поддерживаться
