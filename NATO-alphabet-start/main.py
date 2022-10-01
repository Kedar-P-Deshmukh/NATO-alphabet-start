import  pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")

natodict= { rowdata.letter:rowdata.code for index,rowdata in data.iterrows()}
name=input("enter your name:")
print([natodict[alpha.upper()] for alpha in name])
#ddds