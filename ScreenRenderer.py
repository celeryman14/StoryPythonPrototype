import pygame

screenSize = width, height = 1600, 900

pygame.font.init()
usedFont = pygame.font.SysFont(pygame.font.get_default_font(), 30)
choices = [] # holds button objects

backgroundColour = 0, 0, 0
textColour = 255, 255, 255

class Button:
    def __init__(self, xpos, ypos, name):
        self.x = xpos
        self.y = ypos
        self.name = name
        self.width = usedFont.size(name)[0]
        self.height = usedFont.size("Tg")[1]

    def drawOnScreen(self):
        image = usedFont.render(self.name, 1, textColour)
        screen.blit(image, (self.x, self.y))

    def checkForScreenpress(self, mouse):
        if self.width/2 <= mouse[0] <= self.width/2+140 and self.height/2 <= mouse[1] <= self.height/2+40:
            return True
        return False

            
def ChangeRenderedText(text, choiceNames): #easy way to change the text
    screen.fill(backgroundColour)
    drawText(screen, text, textColour, pygame.Rect((0, 0), (1600, 900 - usedFont.size("Tg")[1])), usedFont, choiceNames)

# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def drawText(surface, text, color, rect, font, choiceNames, aa=False, bkg=None):
    choices.clear()
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing
        text = text[i:]
    x = 0
    
    for i in choiceNames:
          choices.append(Button(x, y, i))
          x += usedFont.size(i)[0] + 20

    for i in choices:
         i.drawOnScreen()
 
    return choices


screen = pygame.display.set_mode(screenSize)
running = True
ChangeRenderedText("placeholder text", ["aaa", "aaaa"])
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN
            mouse = pygame.mouse.get_pos()
            increment = 0
            for i in choices:
                if i.checkForScreenpress(mouse):
                    

    pygame.display.flip()      
    
pygame.display.quit()
pygame.quit()
