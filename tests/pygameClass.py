import pygame

class Terminal:
    def __init__(self, x, y, width, height, font_size, font_color, bg_color, max_lines=10):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        self.font_color = font_color
        self.bg_color = bg_color
        self.max_lines = max_lines
        self.lines = []
        self.font = pygame.font.SysFont(None, font_size)
        self.text_surface = pygame.Surface((width, height))
        self.scroll_pos = 0
        self.scroll_speed = 5

    def add_line(self, text):
        self.lines.append(text)
        if len(self.lines) > self.max_lines:
            self.lines.pop(0)
        self.scroll_pos = 0

    def scroll_up(self):
        if len(self.lines) > self.max_lines:
            self.scroll_pos += self.scroll_speed
            if self.scroll_pos > (len(self.lines) - self.max_lines) * self.font_size:
                self.scroll_pos = (len(self.lines) - self.max_lines) * self.font_size

    def scroll_down(self):
        if self.scroll_pos > 0:
            self.scroll_pos -= self.scroll_speed
            if self.scroll_pos < 0:
                self.scroll_pos = 0

    def draw(self, screen):
        self.text_surface.fill(self.bg_color)
        for i, line in enumerate(self.lines):
            if i < len(self.lines) - self.max_lines or i >= len(self.lines) - self.max_lines + int(self.scroll_pos / self.font_size):
                continue
            text_surface = self.font.render(line, True, self.font_color)
            self.text_surface.blit(text_surface, (0, i * self.font_size - self.scroll_pos))
        pygame.draw.rect(screen, self.bg_color, (self.x, self.y, self.width, self.height))
        screen.blit(self.text_surface, (self.x, self.y))
        pygame.draw.rect(screen, self.font_color, (self.x, self.y, self.width, self.height), 1)
