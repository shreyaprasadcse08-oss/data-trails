Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
Traceback (most recent call last):
  File "C:\Users\shreya prasad\Desktop\data_trails.py", line 19, in <module>
    students = pd.read_csv("student_marks_messy.csv")
  File "C:\Users\shreya prasad\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\shreya prasad\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\shreya prasad\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\shreya prasad\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\shreya prasad\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\common.py", line 930, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'student_marks_messy.csv'

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60
gender
Female    474
Male      434
f          18
MALE       15
M          13
m          12
FEMALE     10
F           9
female      8
male        7
Name: count, dtype: int64

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60
gender
Female    474
Male      434
f          18
MALE       15
M          13
m          12
FEMALE     10
F           9
female      8
male        7
Name: count, dtype: int64
gender
Female    519
Male      481
Name: count, dtype: int64

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60
gender
Female    474
Male      434
f          18
MALE       15
M          13
m          12
FEMALE     10
F           9
female      8
male        7
Name: count, dtype: int64
gender
Female    519
Male      481
Name: count, dtype: int64

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60
gender
Female    474
Male      434
f          18
MALE       15
M          13
m          12
FEMALE     10
F           9
female      8
male        7
Name: count, dtype: int64
gender
Female    519
Male      481
Name: count, dtype: int64
str

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60
gender
Female    474
Male      434
f          18
MALE       15
M          13
m          12
FEMALE     10
F           9
female      8
male        7
Name: count, dtype: int64
gender
Female    519
Male      481
Name: count, dtype: int64
str
Traceback (most recent call last):
  File "pandas/_libs/lib.pyx", line 2478, in pandas._libs.lib.maybe_convert_numeric
ValueError: Unable to parse string "91 marks"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\shreya prasad\Desktop\data_trails.py", line 37, in <module>
    students["english_marks"] = pd.to_numeric(students["english_marks"])
  File "C:\Users\shreya prasad\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\tools\numeric.py", line 235, in to_numeric
    values, new_mask = lib.maybe_convert_numeric(  # type: ignore[call-overload]
  File "pandas/_libs/lib.pyx", line 2521, in pandas._libs.lib.maybe_convert_numeric
ValueError: Unable to parse string "91 marks" at position 12

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60
gender
Female    474
Male      434
f          18
MALE       15
M          13
m          12
FEMALE     10
F           9
female      8
male        7
Name: count, dtype: int64
gender
Female    519
Male      481
Name: count, dtype: int64
str
Traceback (most recent call last):
  File "pandas/_libs/lib.pyx", line 2478, in pandas._libs.lib.maybe_convert_numeric
ValueError: Unable to parse string "sixty"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\shreya prasad\Desktop\data_trails.py", line 38, in <module>
    students["english_marks"] = pd.to_numeric(students["english_marks"])
  File "C:\Users\shreya prasad\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\tools\numeric.py", line 235, in to_numeric
    values, new_mask = lib.maybe_convert_numeric(  # type: ignore[call-overload]
  File "pandas/_libs/lib.pyx", line 2521, in pandas._libs.lib.maybe_convert_numeric
ValueError: Unable to parse string "sixty" at position 29

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60
gender
Female    474
Male      434
f          18
MALE       15
M          13
m          12
FEMALE     10
F           9
female      8
male        7
Name: count, dtype: int64
gender
Female    519
Male      481
Name: count, dtype: int64
str
<StringArray>
[          '46',           '88',           '44',           '85',
           '60',           '78',           '50',           '65',
           '83',           '71',           '95',            nan,
     '91 marks',           '70',           '47',           '56',
           '34',           '53',           '57',           '33',
           '74',           '98',           '90',           '45',
           '59',           '43',        'sixty',          '100',
           '81',           '87',           '97',           '92',
           '30',           '61',           '52',           '36',
           '39',           '48',           '84',           '94',
           '37',           '68',           '66',           '26',
           '29',     '72 marks',           '69',           '64',
           '76',           '86',           '54',           '49',
           '99',           '63',           '80',           '91',
           '28',           '62',           '38',           '42',
           '25',           '32',     '95 marks',           '55',
           '77',           '89',           '93',           '72',
           '73',     '96 marks',       'eighty',           '79',
           '96', 'seventy five',           '41',           '67',
           '35',           '58',           '31',           '75',
           '82',           '27',           '40',     '80 marks',
     '82 marks',           '51',     '49 marks',     '58 marks',
     '61 marks',     '84 marks',     '63 marks',     '76 marks',
     '99 marks',    '100 marks']
Length: 94, dtype: str
str

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60
gender
Female    474
Male      434
f          18
MALE       15
M          13
m          12
FEMALE     10
F           9
female      8
male        7
Name: count, dtype: int64
gender
Female    519
Male      481
Name: count, dtype: int64
float64

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60
gender
Female    474
Male      434
f          18
MALE       15
M          13
m          12
FEMALE     10
F           9
female      8
male        7
Name: count, dtype: int64
gender
Female    519
Male      481
Name: count, dtype: int64
float64
5
(995, 6)

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60
gender
Female    474
Male      434
f          18
MALE       15
M          13
m          12
FEMALE     10
F           9
female      8
male        7
Name: count, dtype: int64
gender
Female    519
Male      481
Name: count, dtype: int64
float64
5
(995, 6)
student_id          0
gender              0
math_marks         17
physics_marks      14
chemistry_marks    22
english_marks      10
dtype: int64

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60
gender
Female    474
Male      434
f          18
MALE       15
M          13
m          12
FEMALE     10
F           9
female      8
male        7
Name: count, dtype: int64
gender
Female    519
Male      481
Name: count, dtype: int64
float64
5
(995, 6)
student_id          0
gender              0
math_marks         17
physics_marks      14
chemistry_marks    22
english_marks      10
dtype: int64
student_id         0
gender             0
math_marks         0
physics_marks      0
chemistry_marks    0
english_marks      0
dtype: int64

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60
gender
Female    474
Male      434
f          18
MALE       15
M          13
m          12
FEMALE     10
F           9
female      8
male        7
Name: count, dtype: int64
gender
Female    519
Male      481
Name: count, dtype: int64
float64
5
(995, 6)
student_id          0
gender              0
math_marks         17
physics_marks      14
chemistry_marks    22
english_marks      10
dtype: int64
student_id         0
gender             0
math_marks         0
physics_marks      0
chemistry_marks    0
english_marks      0
dtype: int64
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age              0
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60
gender
Female    474
Male      434
f          18
MALE       15
M          13
m          12
FEMALE     10
F           9
female      8
male        7
Name: count, dtype: int64
gender
Female    519
Male      481
Name: count, dtype: int64
float64
5
(995, 6)
student_id          0
gender              0
math_marks         17
physics_marks      14
chemistry_marks    22
english_marks      10
dtype: int64
student_id         0
gender             0
math_marks         0
physics_marks      0
chemistry_marks    0
english_marks      0
dtype: int64
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age              0
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
Pclass
1    84.154687
2    20.662183
3    13.675550
Name: Fare, dtype: float64
Pclass
1    38.062130
2    29.825163
3    24.824684
Name: Age, dtype: float64
Pclass
1    0.629630
2    0.472826
3    0.242363
Name: Survived, dtype: float64

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60
gender
Female    474
Male      434
f          18
MALE       15
M          13
m          12
FEMALE     10
F           9
female      8
male        7
Name: count, dtype: int64
gender
Female    519
Male      481
Name: count, dtype: int64
float64
5
(995, 6)
student_id          0
gender              0
math_marks         17
physics_marks      14
chemistry_marks    22
english_marks      10
dtype: int64
student_id         0
gender             0
math_marks         0
physics_marks      0
chemistry_marks    0
english_marks      0
dtype: int64
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age              0
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
Pclass
1    84.154687
2    20.662183
3    13.675550
Name: Fare, dtype: float64
Pclass
1    38.062130
2    29.825163
3    24.824684
Name: Age, dtype: float64
Pclass
1    0.629630
2    0.472826
3    0.242363
Name: Survived, dtype: float64
Embarked
S    644
C    168
Q     77
Name: count, dtype: int64

============ RESTART: C:\Users\shreya prasad\Desktop\data_trails.py ============
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
(891, 12)
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
33            34         0       2  ...   10.5000          NaN         S
54            55         0       1  ...   61.9792          B30         C
96            97         0       1  ...   34.6542           A5         C
116          117         0       3  ...    7.7500          NaN         Q
170          171         0       1  ...   33.5000          B19         S
252          253         0       1  ...   26.5500          C87         S
275          276         1       1  ...   77.9583           D7         S
280          281         0       3  ...    7.7500          NaN         Q
326          327         0       3  ...    6.2375          NaN         S
438          439         0       1  ...  263.0000  C23 C25 C27         S
456          457         0       1  ...   26.5500          E38         S
483          484         1       3  ...    9.5875          NaN         S
493          494         0       1  ...   49.5042          NaN         C
545          546         0       1  ...   26.0000          NaN         S
555          556         0       1  ...   26.5500          NaN         S
570          571         1       2  ...   10.5000          NaN         S
625          626         0       1  ...   32.3208          D50         S
630          631         1       1  ...   30.0000          A23         S
672          673         0       2  ...   10.5000          NaN         S
745          746         0       1  ...   71.0000          B22         S
829          830         1       1  ...   80.0000          B28       NaN
851          852         0       3  ...    7.7750          NaN         S

[22 rows x 12 columns]
   PassengerId  ...                                               Name
0            1  ...                            Braund, Mr. Owen Harris
1            2  ...  Cumings, Mrs. John Bradley (Florence Briggs Th...
2            3  ...                             Heikkinen, Miss. Laina
3            4  ...       Futrelle, Mrs. Jacques Heath (Lily May Peel)
4            5  ...                           Allen, Mr. William Henry

[5 rows x 4 columns]
   student_id  gender  math_marks  physics_marks  chemistry_marks english_marks
0        1001    Male        58.0           35.0             89.0            46
1        1002  Female        75.0           69.0             92.0            88
2        1003  Female        74.0           32.0             41.0            44
3        1004       M        60.0           74.0             92.0            85
4        1005    Male        89.0           72.0             33.0            60
gender
Female    474
Male      434
f          18
MALE       15
M          13
m          12
FEMALE     10
F           9
female      8
male        7
Name: count, dtype: int64
gender
Female    519
Male      481
Name: count, dtype: int64
float64
5
(995, 6)
student_id          0
gender              0
math_marks         17
physics_marks      14
chemistry_marks    22
english_marks      10
dtype: int64
student_id         0
gender             0
math_marks         0
physics_marks      0
chemistry_marks    0
english_marks      0
dtype: int64
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age              0
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
Pclass
1    84.154687
2    20.662183
3    13.675550
Name: Fare, dtype: float64
Pclass
1    38.062130
2    29.825163
3    24.824684
Name: Age, dtype: float64
Pclass
1    0.629630
2    0.472826
3    0.242363
Name: Survived, dtype: float64
Embarked
S    644
C    168
Q     77
Name: count, dtype: int64
   PassengerId  Survived  Pclass  ... Cabin Embarked         Port
0            1         0       3  ...   NaN        S  Southampton
1            2         1       1  ...   C85        C    Cherbourg
2            3         1       3  ...   NaN        S  Southampton
3            4         1       1  ...  C123        S  Southampton
4            5         0       3  ...   NaN        S  Southampton

[5 rows x 13 columns]
