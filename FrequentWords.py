#This Program is to print the top 10 most frequently appeearing words in a text file

def count():
    file=open('sample.txt','r')
    word_count={}

    for line in file:
        word=line.lower().split()
        for w in word:
            if w in word_count:
                word_count[w]+=1
            else:
                word_count[w]=1
    file.close()
    for k,v in word_count.items():
        print(f"The Word {k} appears {v} times in the File...")

count()