# 日本カレンダーファインダー

# Date As String (YYYYMMDD)
date_str = input("Enter Date [YYYYMMDD]: ")

# print(len(date_str))

if len(date_str) == 8:
  year = date_str[:4]
  # print(type(year))

  month = date_str[4:6]
  date = date_str[6:]

  # Japanese Calendar Period Finder
  # Ref.: https://homepages.cwi.nl/~aeb/go/misc/jdate.html
  
  # 明治 
  if year >= "1868" and year <= "1911":
    diff_year = int(year) - 1867
    print("明治", diff_year, "年", month, "月", date, "日")

  # 大正
  elif year >= "1912" and year <= "1925":
    diff_year = int(year) - 1911
    print("大正", diff_year, "年", month, "月", date, "日")

  # 昭和
  elif year >= "1926" and year <= "1988":
    diff_year = int(year) - 1925
    print("昭和", diff_year, "年", month, "月", date, "日")
  
  # 平成
  elif year >= "1989" and year <= "2018":
    diff_year = int(year) - 1988
    print("平成", diff_year, "年", month, "月", date, "日")

  # 令和
  else:
    diff_year = int(year) - 2018
    print("令和", diff_year, "年", month, "月", date, "日")
  
  # print(year, "-", month, "-", date)