# Build-a-RPM-Package-from-Source-on-CentOS
Set Up an RPM Build Environment under CentOS: ipyhton-8.5.0, grpcio-1.50.0

Для сборки RPM пакета ipython 8.5.0 в CentOS 8 выполните следующие шаги:

1. Установите необходимые зависимости:
   `` sudo yum install -y openssl-devel ncurses-devel libffi-devel xz-devel libuuid-devel tk-devel gdbm-devel sqlite-devel bzip2-devel readline-devel gcc make rpmdevtools python3-devel python3-setuptools python3-pip ``
2. Создайте директорию для сборки RPM пакета:
   ``rpmdev-setuptree``
3. Загрузите исходный код ipython 8.5.0 в директорию SOURCES:
  `` wget https://files.pythonhosted.org/packages/25/a5/dda90aa8cb931458a357ae65ff4341d7694464f322b095a438489440dc7c/ipython-8.5.0.tar.gz -P ~/rpmbuild/SOURCES/``

4. Создайте файл ipython.spec в директории SPECS и добавьте в него следующее содержимое:


5. Выполните сборку пакета:
``rpmbuild -ba -D 'debug_package %{nil}' ipython.spec ``
``rpmbuild -ba grpcio.spec ``


# Некоторые зависимости которые могут понадобятся:

https://centos.pkgs.org/9-stream/centos-appstream-x86_64/ Здесь можно найти зависимости для сборки RPM

https://dl.fedoraproject.org/pub/epel/8/Everything/x86_64/ 

https://readthedocs.org/projects/python-rpm-porting/downloads/pdf/latest/ Python RPM Porting Guide

https://access.redhat.com/documentation/ru-ru/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/assembly_packaging-python-3-rpms_configuring-basic-system-settings#footnote--CO1-5 документация для сборки

https://chaidas.com/index.php?controller=post&action=view&id_post=130 Если нужен python 3.9 rpm пакет

