#!/usr/bin/env python3
''' This is a simple webbrowser for the command line '''

import selenium
from selenium import webdriver
import sys
import time
import os
import requests
from bs4 import BeautifulSoup

import click
from tld import get_tld
import escapecodes
import curses


class Browser():
    def __init__(self):
        ''' Initalizes all of the variables, takes no arguments '''
        self.browser = webdriver.Chrome()
        self.screen = curses.initscr()
        self.output = curses.newpad(20,20 )
        self.history = []
        self.url = ''
        self.domain = ''
        self.body = []
        self.page_links = []
        self.selected_link = ''
        self.search_query = ''
        self.ansi = escapecodes.Ansi()
        self.get_url()
        self.get_webpage()
        print(self.ansi.color_list)

    def get_url(self):
        ''' Gets the desired url from the user '''
        self.url = 'https://realpython.com' #input('[Enter a Url]: ')
        self.domain = f'https://{get_tld(self.url, as_object=True).fld}'
        print(self.domain)

    def get_webpage(self):
        ''' Gets the selected webpage '''
        self.browser.get(self.url)
        self.history.append(self.url)
        print(self.history)
        self.process_webpage_links()

    def process_webpage_links(self):
        ''' Processes the current webpage '''
        self.html = BeautifulSoup(self.browser.page_source,'html.parser')
        self.page_links = self.html.find_all('a')
        for a in self.html.find_all('a'):
            try:
                a.string = f'{self.ansi.color("br_blue")}[{self.page_links.index(a)}]{a.text.lstrip()}{self.ansi.reset}'
                #print(a.string)
            except Exception as e:
                print(e)
                continue
        self.body = self.html.find('body')
        # for i in self.body:
        #     print(i.text,i.attrs)
        #     x = input()

    def clicked_link(self):
        try:
            if self.selected_link.get('href') and not self.selected_link.get('href').startswith('http'):
                #print(self.selected_link.get('href'))
                self.url = (f'{self.domain}{self.selected_link.get("href")}')
                self.get_webpage()
            elif self.selected_link.get('href'):
                #print(self.selected_link.get('href'))
                self.url = (self.selected_link.get('href'))
                self.domain = f'https://{get_tld(self.url, as_object=True).fld}'

                self.get_webpage()

        except Exception as e:
            print(e)
            #print(self.selected_link)
            #print(self.selected_link.get('href'))

    def search(self):
        self.url = f'https://google.com/search?q={self.search_query}'
        self.domain = f'https://{get_tld(self.url, as_object=True).fld}'
        self.get_webpage()
    def back_button(self):
        self.url = self.history[-2]
        self.domain = f'https://{get_tld(self.url, as_object=True).fld}'

        self.history.pop(-1)
        self.history.pop(-1)

    def display(self):
        print(self.ansi.effects('clr_scr'))
        #for i in self.page_links:
           #print(f'[{self.page_links.index(i)}]{i.text}')
        self.body2 = self.body.find_all()
    #    self.body2 = set(self.body2)
    #    print(len(self.body2))
        for i in self.body2:
            #i = i.text.split('\n')
            #for j in i:
            #if i.p or i.a or i.title or i.h1:
            #    if i.h1:
            #        print(self.ansi.color('br_red'),i.text,self.ansi.reset)
                try:
                    self.output.addstr(0,0,'i.text')


                    self.output.refresh(0,0,0,0,80,640)
                except Exception as e:
                    print (e)
                    pass
        curses.napms(3000)
main = Browser()
main.display()
while True:
    key = click.getchar()
    print(key)
    if key == '=':
        link_number = input('[Enter Link Number]: ')
        main.selected_link = main.page_links[int(link_number)]
        main.clicked_link()
        main.display()
    if key == '`':
        main.search_query = input('[Enter Search]: ')
        main.search()
        main.display()
    if key == 'b':
        main.back_button()
        main.get_webpage()
        main.display()
