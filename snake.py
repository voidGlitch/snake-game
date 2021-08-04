from turtle import Turtle, screensize

STARTING_POSITION = [ (0,0),(-20,0),(-40,0) ]   #constants are always in capital letters
MOVE_DISTANCE =20
UP =90
DOWN = 270
LEFT= 180
RIGHT =0 

class Snake:
    def __init__(self) -> None:
        self.segments=[]
        self.Create_snake()
        self.head = self.segments[0]
    
    def Create_snake(self):
        for positions in STARTING_POSITION:
            self.add_segment(positions)
            
    def add_segment(self,positions):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(positions)
        self.segments.append(new_segment)


    def extend(self):
        self.add_segment(self.segments[-1].position())  #-1 returns the last position of the current list and position() is a method in turtle module which return the x,y position
    
    def move(self):
        
        for seg_num in range (len(self.segments)-1,0,-1):   #range() takes no keyword arguments
            new_x = self.segments[seg_num-1].xcor()   # takes cordinates from  the next segment because we are dealing in reverse order
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)   # set the cordinate of previous segment to the next segment
        self.segments[0].forward(MOVE_DISTANCE)

    # def up(self):
    #     for seg_num in range(len(self.segments)-1,0,1):
    #         new_x =self.segments[seg_num -1].xcor()
    #         new_y =self.segments[seg_num -1].ycor()
    #         self.segments[seg_num].goto(new_x,new_y)
    #     self.segments[0].setheading(90) 

    # def down(self):
    #     for seg_num in range(len(self.segments)-1,0,1):
    #         new_x =self.segments[seg_num -1].xcor()
    #         new_y =self.segments[seg_num -1].ycor()
    #         self.segments[seg_num].goto(new_x,new_y)
    #     self.segments[0].setheading(270) 


    # def left(self):
    #     for seg_num in range(len(self.segments)-1,0,1):
    #         new_x =self.segments[seg_num -1].xcor()
    #         new_y =self.segments[seg_num -1].ycor()
    #         self.segments[seg_num].goto(new_x,new_y)
    #     self.segments[0].setheading(180) 


    # def right(self):
    #     for seg_num in range(len(self.segments)-1,0,1):
    #         new_x =self.segments[seg_num -1].xcor()
    #         new_y =self.segments[seg_num -1].ycor()
    #         self.segments[seg_num].goto(new_x,new_y)
    #     self.segments[0].setheading(360) 
        
    def up(self):
        if self.head.heading() != DOWN:   # IF our heading is not equal to down i.e 90 != 270 then okay else if our heading is 270 != 270 then the following code will not performed
            self.head.setheading(UP)     


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN) 


    def left(self):
        if self.head.heading() != RIGHT:  #sAME GOES FOR ALL
            self.head.setheading(LEFT)  

            
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)  