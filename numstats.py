
newCalculation = True;
while newCalculation:

    sum = 0;
    count = 0;
    fileName = str(input("What is the name of the file you want to open: "));
    try:
        f = open(fileName, "r");
        #print("list of random numbers in random.txt: ");
        max = 0;
        min = 10;
        for x in f:
            #print(x)
            #num = int(x)
            
            num = int(x.split(",")[0])
            #print("min: ", num);
            if (max <= num):
                max = num
                #print("min: ", max);
            if (min > num):
                min = num;
                #print("min: ", num);
            
            sum += int(x);
            count += 1;
            average = sum / count;
            range = max - min;
        #numbers = [float(line.rstrip()) for line in f]
        #smallest = min(numbers);
        print("FileName: ", fileName);
        print("Sum: ", sum);
        print("count: ",count);
        print("Average: ", average);
        print("Max: ", max);
        print("Min: ", min);
        print("Range: ", range);
   
        again = input("If you want to play again type y: ");
        if again != "y":
            newCalculation = False;
   
    except IOError:
        print("There is no file named randomnum.txt");

    


  
