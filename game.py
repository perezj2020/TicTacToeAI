from player import HumanPlayer, NPC
class tictactoe:
    def __init__(self):
        self.board=[' ' for _ in range(9)] #single 3x3 board
        self.currentwin= None # winner count

    def printboard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row)+' |')

    @staticmethod
    def printboardnumbers():
        #0\1\2 number to spot
        numberboard=[[str(i) for i in range (j*3, (j+1)*3)] for j in range(3)]
        for row in numberboard:
            print('| '+' | '.join(row)+' |')

    def availablemoves(self):
      return [i for i, spot in enumerate(self.board) if spot == ' ']
    def emptysquares(self):
        return ' ' in self.board
    def emptysquaresspaces(self):
        return self.board.count(' ')
    def makemove (self, square, letter):
        if self.board[square] == ' ':
            self.board[square]=letter
            if self.winner(square,letter):
                self.currentwin=letter
            return True
        else:
            False
    def winner(self,square,letter):
        rowindex=square//3
        row=self.board[rowindex*3 : (rowindex+1)*3]
        if all([spot==letter for spot in row]):
            return True
        colindex=square%3
        column=[self.board[colindex+i*3] for i in range(3)]
        if all ([spot==letter for spot in column]):
            return True
        if square%2==0:
            diagonal1=[self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False
    def reset(self,square,letter):
        i=0
        while i!=9:
            self.board[i]=' '
            i=i+1
        return True




def play (game,xplayer,oplayer,printgame=True):
    if printgame:
        game.printboardnumbers()
    letter='X'
    endgame = True
    #iterate while empty squares are available
    while game.emptysquares() and endgame == True:
        if letter =='O':
            square = oplayer.getmove(game)
        else:
            square = xplayer.getmove(game)
        if game.makemove(square,letter):
            if printgame:
                print(letter + f' makes a move to square {square}')
                game.printboard()
                print('')
            if game.currentwin:
                if printgame:
                    print(letter+' WINS')
                    game.reset(square,letter)
                    game.currentwin = None
                return letter

            if letter=='X':
                letter='O'
            else :
                letter='X'

    if printgame:
        print("TIE")
        game.reset(square, letter)




if __name__ =='__main__':
    xplayer= HumanPlayer('X')
    oplayer= NPC('O')
    t= tictactoe()
    endgame=False
    
    while endgame==False:
        play(t,xplayer,oplayer,printgame=True)
        again=input('Play again? Y OR N')
        again=again.lower()
        if again=='n':
            print("Thanks for Playing!")
            endgame=True
        elif again=='y':
            endgame=False
        else:
            print('Invalid input, restarting game')
            
                #Comment out the while loop to test AI vs Random NPC with this code
   ''' 
   if __name__ =='__main__':
    xwins=0
    owins=0
    ties=0
    for _ in range(100):
        xplayer= RNPC('X')
        oplayer= NPC('O')
        t= tictactoe()
        result= play(t,xplayer,oplayer,printgame=False)
        if result=='X':
            xwins+=1
        elif result=='O':
            owins+=1
        else:
            ties+=1
    print(f'X wins= {xwins}, O wins: {owins}, Ties: {ties}')
    '''




