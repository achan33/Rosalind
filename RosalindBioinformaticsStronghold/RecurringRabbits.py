import argparse
'''
This program takes in txt file with n= months and k= pairs of rabbits producing offsprings.
Recurrence Relation is the recursive calculation of the current term based on the previous term
Fibonacci is an example of reccurrence

'''
def recurr(months, offspring ):
    #starting pair
    if(months == 1):
        return 1
    #if offspring of 1 pair is 3 return as n =2 , 3 
    elif(months == 2):
        return offspring
    pgen1 =recurr(months -1 , offspring)
    pgen2 =recurr(months-2 , offspring)
    if(months <=4):
        return pgen1 +pgen2   
    return(pgen1 +(pgen2 * offspring)) 

def test(args):
    infile = open(args)
    val = infile.readline()
    n = val.split(' ')
    months = n[0]
    os = n[1]
    data= [ months, os]
    return data



def main():
    parser = argparse.ArgumentParser(description = "Take in file for reccurence relation")
    parser.add_argument('-i', '--input_file' , type = str, help= 'Read in input file')
    parser.add_argument('-o', '--output_file', type = str, help = 'Create output file')

    args = parser.parse_args()
    a = test(args.input_file)
    val = recurr(int(a[0]) , int(a[1]))
    #print(val)
    with open(args.output_file , 'w') as out:
        out.write(str(val))
      

if __name__ == '__main__':
    main()
else:
    print("Program could not execute")
