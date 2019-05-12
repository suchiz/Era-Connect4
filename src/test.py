import unittest
from connect4 import *

class Test(unittest.TestCase):


    def test_addToken2(self):
        board = Board()
        add1= board.add_token2(1)
        add2= board.add_token2(1)
        add3 = board.add_token2(2)
        self.assertEqual(add1,(0,1,1))
        #player 2 put token above the previous one
        self.assertEqual(add2,(1,1,2))
        #plater 1 turn
        self.assertEqual(add3,(0,2,1))
   
    def test_isValid(self):
        board = Board()
        self.assertTrue(board.isValid(0))
        self.assertTrue(board.isValid(1))
        self.assertTrue(board.isValid(2))
        self.assertTrue(board.isValid(3))
        self.assertTrue(board.isValid(4))
        self.assertTrue(board.isValid(5))
        self.assertTrue(board.isValid(6))
        
    
        #add 1 token to a column = not full

        board.add_token2(1)
        self.assertTrue(board.isValid(1))

        #add 6 tokens to column 2 = full
        board.add_token2(2)
        board.add_token2(2)
        board.add_token2(2)
        board.add_token2(2)
        board.add_token2(2)
        board.add_token2(2)
        self.assertFalse(board.isValid(2))


    def test_get_row_from_column(self):
        board = Board()

        t1 = board.get_row_from_column(1)
        self.assertEqual(0,t1)

        board.add_token2(1)

        t2 = board.get_row_from_column(1)
        self.assertEqual(1,t2)

    def test_getValidMoves(self):
        board = Board()

        t1 = board.getValidMoves()
        self.assertEqual([0,1,2,3,4,5,6],t1)


        board.add_token2(1)
        t2 = board.getValidMoves()
        self.assertEqual([0,1,2,3,4,5,6],t2)

        #Column 2 full so not a valid move
        board.add_token2(2)
        board.add_token2(2)
        board.add_token2(2)
        board.add_token2(2)
        board.add_token2(2)
        board.add_token2(2)
        t3=board.getValidMoves()
        self.assertEqual([0,1,3,4,5,6],t3)


  

    def test_add_token(self):

        board = Board()
        add1= board.add_token([1200,900],20,300)
        self.assertEqual((0,3,1),add1)



    def test_check_win(self):
        board = Board()

        # nothing
        self.assertEqual(0,board.check_win())
        
        #check column win (all token same colour)
        board.add_token2(2)
        self.assertEqual(0,board.check_win())
        
        board.turn=1
        board.add_token2(2)
        board.turn=1
        board.add_token2(2)
        board.turn=1
        board.add_token2(2)
        self.assertNotEqual(0,board.check_win())
        
        #check row win (all tokens same colour)
        board = Board()
        board.add_token2(2)
        board.turn=1
        board.add_token2(3)
        board.turn=1
        board.add_token2(4)
        self.assertEqual(0,board.check_win())
        board.turn=1
        board.add_token2(5)
        self.assertNotEqual(0,board.check_win())
        

        #check diagonal win
        board = Board()
        board.add_token2(2) #p1
        board.add_token2(3) #p2
        board.add_token2(3) #p1
        board.add_token2(4) #p2
        board.add_token2(4) #p1
        board.add_token2(5) #p2
        board.add_token2(4) #p1
        board.add_token2(5) #p2
        board.add_token2(5) #p1
        board.add_token2(6) #p2
        board.add_token2(5) #p2

        #add 4 tokens same column (not same colour = no winner)
        board = Board()
        board.add_token2(2) #p1
        board.add_token2(2) #p2
        board.add_token2(2) #p1
        board.add_token2(2) #p2
        self.assertEqual(0,board.check_win())

        #add 4 tokens same row (not same colour = no winner)
        board = Board()
        board.add_token2(2) #p1
        board.add_token2(3) #p2
        board.add_token2(4) #p1
        board.add_token2(5) #p2
        self.assertEqual(0,board.check_win())

         #check  4 tokens in diagonal not same colour
        board = Board()
        board.add_token2(2) #p1
        board.add_token2(3) #p2
        board.add_token2(3) #p1
        board.add_token2(4) #p2
        board.add_token2(4) #p1
        board.add_token2(4) #p2
        board.add_token2(5) #p1
        board.add_token2(5) #p2
        board.add_token2(5) #p1
        board.add_token2(5) #p2
        self.assertEqual(0,board.check_win())


    def test_check_win2(self):
        board = Board()
        #no winner cause nothing on board
        self.assertFalse(board.check_win2())


    def test_check_draw(self):
        board = Board()
        
        self.assertEqual(0,board.check_draw())
        board.add_token2(2)

        self.assertEqual(0,board.check_draw())

        board.board =  np.ones((board.ROWS, board.COLS))
        self.assertEqual(1,board.check_draw())


        #add 4 same colour token in row to check win2
        board.add_token2(2)
        board.turn=1
        board.add_token2(3)
        board.turn=1
        board.add_token2(4)
        board.turn=1
        board.add_token2(5)
        self.assertTrue(board.check_win2())


    def test_computeCoinDatas(self):
       
        board = Board()
        add1= board.computeCoinDatas([1200,900],20,300)
        self.assertEqual((0,3,1),add1)


    def test_isValid2(self):

        board = Board()

        self.assertTrue(board.isValid2(0,0))
        self.assertTrue(board.isValid2(5,6))
        self.assertFalse(board.isValid2(1,7))
        self.assertFalse(board.isValid2(6,2))
        self.assertFalse(board.isValid2(-6,2))
        self.assertFalse(board.isValid2(6,-1))


if __name__ == '__main__':
    unittest.main()