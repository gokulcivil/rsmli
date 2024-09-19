
import imp
from re import M
from myPackage import mymodule

from myPackage import add
import pathlib as Path

mymodule.myfunc()
file_path = r"D:\SAB\01.RSMLI\17.Daily Progress Report\425\Manpower Category.csv"
df = add.manpower_category(man_catg_filepath=file_path)
print(df.head())


