from experta import *


class AgeRange(Fact):
    pass

class Guide(KnowledgeEngine):

    @Rule(NOT(AgeRange(W())), salience=51)
    def ageRange(self):
        self.declare(AgeRange(input("What is your age range? ")))

    @Rule(AgeRange(P(lambda x: int(x) > 45)), AgeRange(W()), salience=50)
    def old(self):
        self.declare(Fact(Healthy='n'))

    @Rule(AgeRange(P(lambda x:int(x) <= 45 )), AgeRange(P(lambda x:int(x) >= 18 )), salience=50)
    def young(self):
        ans= input("Do you have any physical disabilities or special needs( y/n )? ")
        self.declare(Fact(SpecialNeeds=ans))

    @Rule(Fact(SpecialNeeds="y"), salience=49)
    def specialneeds(self):
        self.declare(Fact(Healthy='n'))


    @Rule(Fact(SpecialNeeds="n"), salience=49)
    def healthy(self):
        self.declare(Fact(Healthy='y'))
        
    @Rule(salience=48)
    def history(self):
        ans= input("Are you interested in historical sites ( y/n )? ")
        self.declare(Fact(History=ans))

    @Rule(salience=47)
    def religion(self):
        ans= input("Are you interested in religious sites ( y/n )? ")
        self.declare(Fact(Religion=ans))

    @Rule(salience=46)
    def culture(self):
        ans= input("Are you interested in cultural sites ( y/n )? ")
        self.declare(Fact(Culture=ans))

    @Rule(salience=45)
    def nature(self):
        ans= input("Are you interested in natural sites ( y/n )? ")
        self.declare(Fact(Nature=ans))

    @Rule(salience=44)
    def entertainment(self):
        ans= input("Are you interested in entertainment sites ( y/n )? ")
        self.declare(Fact(Entertainment=ans))

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res1(self):
        print('Here is a List of recommended sites: \n')
        file = open('res1.txt', 'r')
        # This will print every line one by one in the file
        for each in file:
         print (each)
        
    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res2(self):
        print('Here is a List of recommended sites: \n')
        file = open('res2.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res3(self):
        print('Here is a List of recommended sites: \n')
        file = open('res3.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res4(self):
        print('Here is a List of recommended sites: \n')
        file = open('res4.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res5(self):
        print('Here is a List of recommended sites: \n')
        file = open('res5.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res6(self):
        print('Here is a List of recommended sites: \n')
        file = open('res6.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res7(self):
        print('Here is a List of recommended sites: \n')
        file = open('res7.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res8(self):
        print('Here is a List of recommended sites: \n')
        file = open('res8.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res9(self):
        print('Here is a List of recommended sites: \n')
        file = open('res9.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res10(self):
        print('Here is a List of recommended sites: \n')
        file = open('res10.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res11(self):
        print('Here is a List of recommended sites: \n')
        file = open('res11.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res12(self):
        print('Here is a List of recommended sites: \n')
        file = open('res12.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res13(self):
        print('Here is a List of recommended sites: \n')
        file = open('res13.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res14(self):
        print('Here is a List of recommended sites: \n')
        file = open('res14.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res15(self):
        print('Here is a List of recommended sites: \n')
        file = open('res15.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res16(self):
        print('Here is a List of recommended sites: \n')
        file = open('res16.txt', 'r')
        for each in file:
         print (each)

    #second 16
    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res17(self):
        print('Here is a List of recommended sites: \n')
        file = open('res17.txt', 'r')
        # This will print every line one by one in the file
        for each in file:
         print (each)
        
    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res18(self):
        print('Here is a List of recommended sites: \n')
        file = open('res18.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res19(self):
        print('Here is a List of recommended sites: \n')
        file = open('res19.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res20(self):
        print('Here is a List of recommended sites: \n')
        file = open('res20.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res21(self):
        print('Here is a List of recommended sites: \n')
        file = open('res21.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res22(self):
        print('Here is a List of recommended sites: \n')
        file = open('res22.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res23(self):
        print('Here is a List of recommended sites: \n')
        file = open('res23.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res24(self):
        print('Here is a List of recommended sites: \n')
        file = open('res24.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res25(self):
        print('Here is a List of recommended sites: \n')
        file = open('res25.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res26(self):
        print('Here is a List of recommended sites: \n')
        file = open('res26.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res27(self):
        print('Here is a List of recommended sites: \n')
        file = open('res27.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res28(self):
        print('Here is a List of recommended sites: \n')
        file = open('res28.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res29(self):
        print('Here is a List of recommended sites: \n')
        file = open('res29.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res30(self):
        print('Here is a List of recommended sites: \n')
        file = open('res30.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res31(self):
        print('Here is a List of recommended sites: \n')
        file = open('res31.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res32(self):
        file = open('res32.txt', 'r')
        for each in file:
         print (each)

    #no walking
    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res33(self):
        print('Here is a List of recommended sites: \n')
        file = open('res33.txt', 'r')
        # This will print every line one by one in the file
        for each in file:
         print (each)
        
    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res34(self):
        print('Here is a List of recommended sites: \n')
        file = open('res34.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res35(self):
        print('Here is a List of recommended sites: \n')
        file = open('res35.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res36(self):
        print('Here is a List of recommended sites: \n')
        file = open('res36.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res37(self):
        print('Here is a List of recommended sites: \n')
        file = open('res37.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res38(self):
        print('Here is a List of recommended sites: \n')
        file = open('res38.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res39(self):
        print('Here is a List of recommended sites: \n')
        file = open('res39.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res40(self):
        print('Here is a List of recommended sites: \n')
        file = open('res40.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res41(self):
        print('Here is a List of recommended sites: \n')
        file = open('res41.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res42(self):
        print('Here is a List of recommended sites: \n')
        file = open('res42.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res43(self):
        print('Here is a List of recommended sites: \n')
        file = open('res43.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res44(self):
        print('Here is a List of recommended sites: \n')
        file = open('res44.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res45(self):
        print('Here is a List of recommended sites: \n')
        file = open('res45.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res46(self):
        print('Here is a List of recommended sites: \n')
        file = open('res46.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res47(self):
        print('Here is a List of recommended sites: \n')
        file = open('res47.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res48(self):
        print('Here is a List of recommended sites: \n')
        file = open('res48.txt', 'r')
        for each in file:
         print (each)

    #last 16
    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res49(self):
        print('Here is a List of recommended sites: \n')
        file = open('res49.txt', 'r')
        # This will print every line one by one in the file
        for each in file:
         print (each)
        
    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res50(self):
        print('Here is a List of recommended sites: \n')
        file = open('res50.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res51(self):
        print('Here is a List of recommended sites: \n')
        file = open('res51.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res52(self):
        print('Here is a List of recommended sites: \n')
        file = open('res52.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res53(self):
        print('Here is a List of recommended sites: \n')
        file = open('res53.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res54(self):
        print('Here is a List of recommended sites: \n')
        file = open('res54.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res55(self):
        print('Here is a List of recommended sites: \n')
        file = open('res55.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res56(self):
        print('Here is a List of recommended sites: \n')
        file = open('res56.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res57(self):
        print('Here is a List of recommended sites: \n')
        file = open('res57.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res59(self):
        print('Here is a List of recommended sites: \n')
        file = open('res59.txt', 'r')
        for each in file:
         print (each)


    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res61(self):
        print('Here is a List of recommended sites: \n')
        file = open('res61.txt', 'r')
        for each in file:
         print (each)

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res63(self):
        print('Here is a List of recommended sites: \n')
        file = open('res63.txt', 'r')
        for each in file:
         print (each)

g = Guide()
g.reset()
g.run()

