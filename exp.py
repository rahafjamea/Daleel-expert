from experta import *
import math


class AgeRange(Fact):
    pass

class Guide(KnowledgeEngine):
    @staticmethod
    def _output(file):
        print('Here is a List of recommended sites: \n')
        content= file.readlines()
        result={}
        for i in range(0,pace*days,pace):
            site=[]
            for j in range(i,i+pace):
               site.append(content[j].strip())
            tt={"Day":math.ceil(i/pace+1), "Sites": site}
            result.update(tt)
            print(result)

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

    @Rule(Fact(History='y'),Fact(Religion='y'),salience=46)
    def package(self):
        ans= input("Would you like to continue with the historical and religious sites package? ( y/n )? ")
        self.declare(Fact(Package=ans))

    @Rule(Fact(Package="y"),Fact(Healthy="y"), salience=45)
    def history_cat_healthy(self):
        ans= input("Which of these historical sites are you interested in? (You can enter more than one seperated by a comma)\n 1. Museums, Old Houses and Palaces \n 2. Old Markets \n 3. Hisotical Monuments \n ")
        ans=ans.replace(" ", "")
        self.declare(Fact(HistoryCatHealthy=ans))
        print(ans)

    @Rule(Fact(Package="y"), Fact(Healthy="n"), salience=45)
    def history_cat_non_healthy(self):
        ans= input("Which of these historical sites are you interested in? (You can enter more than one seperated by a comma)\n 1. Museums, Old Houses and Palaces \n 2. Hisotical Monuments \n ")
        ans=ans.replace(" ", "")
        self.declare(Fact(HistoryCatNonHealthy=ans))
        print(ans)

    @Rule(Fact(Package="y"),salience=44)
    def religion_cat(self):
        ans= input("Which of these religious sites are you interested in? (You can enter more than one seperated by a comma)\n 1. Islamic Religious Sites \n 2. Christian Religious Sites \n ")
        ans=ans.replace(" ", "")
        self.declare(Fact(ReligionCat=ans))
        print(ans)

    @Rule(Fact(Package="n"),salience=43)
    def culture(self):
        ans= input("Are you interested in cultural sites ( y/n )? ")
        self.declare(Fact(Culture=ans))

    @Rule(Fact(Package="n"),salience=42)
    def nature(self):
        ans= input("Are you interested in natural sites ( y/n )? ")
        self.declare(Fact(Nature=ans))

    @Rule(Fact(Package="n"),salience=41)
    def entertainment(self):
        ans= input("Are you interested in entertainment sites ( y/n )? ")
        self.declare(Fact(Entertainment=ans))

    @Rule(salience=40)
    def pace(self):
        ans= input("Would you like your route pace to be? \n n: normal \n s: slow \n")
        self.declare(Fact(Pace=ans))

    @Rule(Fact(Pace="n"), salience=39)
    def space(self):
        print('ahhh')
        global pace
        pace = 5
    @Rule(Fact(Pace="s"), salience=39)
    def npace(self):
        print('ahh')
        global pace
        pace = 3

    @Rule(salience=38)
    def days(self):
        ans= input("How many days are you staying? ")
        global days
        days=int(ans)
        self.declare(Fact(Days=ans))
        print(ans)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='1'),
        Fact(ReligionCat='1')
    )
    def p_res1(self):
        file = open('package res/p_res1.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='1'),
        Fact(ReligionCat='2')
    )
    def p_res2(self):
        file = open('package res/p_res2.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='1'),
        Fact(ReligionCat='1,2')
    )
    def p_res3(self):
        file = open('package res/p_res3.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='2'),
        Fact(ReligionCat='1')
    )
    def p_res4(self):
        file = open('package res/p_res4.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='2'),
        Fact(ReligionCat='2')
    )
    def p_res5(self):
        file = open('package res/p_res5.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='2'),
        Fact(ReligionCat='1,2')
    )
    def p_res6(self):
        file = open('package res/p_res6.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='3'),
        Fact(ReligionCat='1')
    )
    def p_res7(self):
        file = open('package res/p_res7.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='3'),
        Fact(ReligionCat='2')
    )
    def p_res8(self):
        file = open('package res/p_res8.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='3'),
        Fact(ReligionCat='1,2')
    )
    def p_res9(self):
        file = open('package res/p_res9.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='1,2'),
        Fact(ReligionCat='1')
    )
    def p_res10(self):
        file = open('package res/p_res10.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='1,2'),
        Fact(ReligionCat='2')
    )
    def p_res11(self):
        file = open('package res/p_res11.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='1,2'),
        Fact(ReligionCat='1,2')
    )
    def p_res12(self):
        file = open('package res/p_res12.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='1,3'),
        Fact(ReligionCat='1')
    )
    def p_res13(self):
        file = open('package res/p_res13.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='1,3'),
        Fact(ReligionCat='2')
    )
    def p_res14(self):
        file = open('package res/p_res14.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='1,3'),
        Fact(ReligionCat='1,2')
    )
    def p_res15(self):
        file = open('package res/p_res15.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='2,3'),
        Fact(ReligionCat='1')
    )
    def p_res16(self):
        file = open('package res/p_res16.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='2,3'),
        Fact(ReligionCat='2')
    )
    def p_res17(self):
        file = open('package res/p_res17.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='2,3'),
        Fact(ReligionCat='1,2')
    )
    def p_res18(self):
        file = open('package res/p_res18.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='1,2,3'),
        Fact(ReligionCat='1')
    )
    def p_res19(self):
        file = open('package res/p_res19.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='1,2,3'),
        Fact(ReligionCat='2')
    )
    def p_res20(self):
        file = open('package res/p_res20.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(HistoryCatHealthy='1,2,3'),
        Fact(ReligionCat='1,2')
    )
    def p_res21(self):
        file = open('package res/p_res21.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='n'),
        Fact(HistoryCatNonHealthy='1'),
        Fact(ReligionCat='1')
    )
    def p_res22(self):
        file = open('package res/p_res22.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='n'),
        Fact(HistoryCatNonHealthy='1'),
        Fact(ReligionCat='2')
    )
    def p_res23(self):
        file = open('package res/p_res23.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='n'),
        Fact(HistoryCatNonHealthy='1'),
        Fact(ReligionCat='1,2')
    )
    def p_res24(self):
        file = open('package res/p_res24.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='n'),
        Fact(HistoryCatNonHealthy='2'),
        Fact(ReligionCat='1')
    )
    def p_res25(self):
        file = open('package res/p_res25.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='n'),
        Fact(HistoryCatNonHealthy='2'),
        Fact(ReligionCat='2')
    )
    def p_res26(self):
        file = open('package res/p_res26.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='n'),
        Fact(HistoryCatNonHealthy='2'),
        Fact(ReligionCat='1,2')
    )
    def p_res27(self):
        file = open('package res/p_res27.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='n'),
        Fact(HistoryCatNonHealthy='1,2'),
        Fact(ReligionCat='1')
    )
    def p_res28(self):
        file = open('package res/p_res28.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='n'),
        Fact(HistoryCatNonHealthy='1,2'),
        Fact(ReligionCat='2')
    )
    def p_res29(self):
        file = open('package res/p_res29.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='n'),
        Fact(HistoryCatNonHealthy='1,2'),
        Fact(ReligionCat='1,2')
    )
    def p_res30(self):
        file = open('package res/p_res30.txt', 'r')
        Guide._output(file)

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res1(self):
        file = open('res/res1.txt', 'r')
        # This will print every line one by one in the file
        Guide._output(file)
         
        
    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res2(self):
        file = open('res/res2.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res3(self):
        file = open('res/res3.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res4(self):
        file = open('res/res4.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res5(self):
        file = open('res/res5.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res6(self):
        file = open('res/res6.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res7(self):
        file = open('res/res7.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res8(self):
        file = open('res/res8.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res9(self):
        file = open('res/res9.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res10(self):
        file = open('res/res10.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res11(self):
        file = open('res/res11.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res12(self):
        file = open('res/res12.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res13(self):
        file = open('res/res13.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res14(self):
        file = open('res/res14.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res15(self):
        file = open('res/res15.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res16(self):
        file = open('res/res16.txt', 'r')
        Guide._output(file)
         

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
        file = open('res/res17.txt', 'r')
        # This will print every line one by one in the file
        Guide._output(file)
         
        
    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res18(self):
        file = open('res/res18.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res19(self):
        file = open('res/res19.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res20(self):
        file = open('res/res20.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res21(self):
        file = open('res/res21.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res22(self):
        file = open('res/res22.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res23(self):
        
        file = open('res/res23.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res24(self):
        
        file = open('res/res24.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res25(self):
        
        file = open('res/res25.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res26(self):
        
        file = open('res/res26.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res27(self):
        
        file = open('res/res27.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res28(self):
        
        file = open('res/res28.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res29(self):
        
        file = open('res/res29.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res30(self):
        
        file = open('res/res30.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='y'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res31(self):
        
        file = open('res/res31.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res32(self):
        file = open('res/res32.txt', 'r')
        Guide._output(file)
         

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
        
        file = open('res/res33.txt', 'r')
        # This will print every line one by one in the file
        Guide._output(file)
         
        
    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res34(self):
        
        file = open('res/res34.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res35(self):
        
        file = open('res/res35.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res36(self):
        
        file = open('res/res36.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res37(self):
        
        file = open('res/res37.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res38(self):
        
        file = open('res/res38.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res39(self):
        
        file = open('res/res39.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res40(self):
        
        file = open('res/res40.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res41(self):
        
        file = open('res/res41.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res42(self):
        
        file = open('res/res42.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res43(self):
        
        file = open('res/res43.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res44(self):
        
        file = open('res/res44.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res45(self):
        
        file = open('res/res45.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res46(self):
        
        file = open('res/res46.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res47(self):
        
        file = open('res/res47.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='y'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res48(self):
        
        file = open('res/res48.txt', 'r')
        Guide._output(file)
         

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
        
        file = open('res/res49.txt', 'r')
        # This will print every line one by one in the file
        Guide._output(file)
         
        
    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res50(self):
        
        file = open('res/res50.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res51(self):
        
        file = open('res/res51.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res52(self):
        
        file = open('res/res52.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res53(self):
        
        file = open('res/res53.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='n')
    )
    def res54(self):
        
        file = open('res/res54.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res55(self):
        file = open('res/res55.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='y'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='n')
    )
    def res56(self):
        file = open('res/res56.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res57(self):
        file = open('res/res57.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='y'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res59(self):
        file = open('res/res59.txt', 'r')
        Guide._output(file)
         


    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='y'),
        Fact(Entertainment='y')
    )
    def res61(self):
        file = open('res/res61.txt', 'r')
        Guide._output(file)
         

    @Rule(
        Fact(Healthy='n'),
        Fact(History='n'),
        Fact(Religion='n'),
        Fact(Culture='n'),
        Fact(Nature='n'),
        Fact(Entertainment='y')
    )
    def res63(self):
        file = open('res/res63.txt', 'r')
        Guide._output(file)
         

g = Guide()
g.reset()
g.run()

