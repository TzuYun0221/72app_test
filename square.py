while (True):
    #正方形
    print('請輸入邊長')
    count = int(input())
    squares = []
    stars = ''
    stars_blank = ''
    for times in range(count):
        stars = stars + '*  '
        if(times == 0 or times == count-1):
            stars_blank = stars_blank + '*  '
        else:
            stars_blank = stars_blank + '   '
        
    for times in range(count):
        if(times==0 or times==count-1):
            squares.append(stars)
        else:
            squares.append(stars_blank)
    for star in squares:
        print(star)