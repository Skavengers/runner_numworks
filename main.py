from kandinsky import *
from ion import *
from time import *

platforms_zbeub=[[150,150,20,0],[200,150,20,0],[170,130,40,0],[170,110,40,0],[170,90,40,0],[170,70,40,0],[170,50,40,0],[400,200,600,0],[450,5,600,0],[500,180,600,0],[550,25,600,0],[600,160,600,0],[650,45,600,0],[700,140,1500,0],[740,65,1500,0],[1000,85,20,1],[1500,120,20,1],[1550,85,20,1],[1600,120,20,1],[1750,120,60,1],[1800,105,600,1],[1900,40,20,1]]#,[],[]]
platforms_cmon=[[160,250,50,0],[270,150,50,0],[380,100,50,0],[540,50,50,0],[700,100,50,0],[600,30,20,0],[800,200,90,0],[820,40,150,0],[900,20,30,0],[1000,100,20,0],[1050,100,100,0],[1300,100,310,0],[1700,100,20,0],[2000,50,150,0],[2000,200,15,0],[2500,50,200,0],[2500,200,200,0],[2550,70,150,0],[2550,170,150,0],[2800,100,50,0],[2900,50,20,0]]
platforms_oof=[[200,50,200,0],[380,210,1000,1],[400,150,150,0],[600,50,42,0],[850,200,100,0],[150,0,2,0]]#,[]]
platforms_essaie = [[500, 20, 100, 0],[600,150,40,0],[650,30,20,0],[700, 400, 100, 0],[955,180,300,0],[955,200,2000,1],[1055,120,2000,0],[800, 60, 60, 0], [850, 200, 50, 0],[2000,140,400,1],[1800,190,1000,0]]
boost_oof=[[2500,"spider"],[1,"v",6],[3,"spider"],[1000,"v",1],[1000,"arrow"]]#,[],[]]
boost_cmon=[[7,"arrow"],[10,"v",9],[1,(100,150,255)],[1700,"arrow"],[10,"v",7],[50,(90,100,255)],[1500,"arrow"],[50,"v",3],[80,(50,70,200)],[50,"cperso",(255,255,200)],[500,"arrow"],[1500,(40,50,150)],[1,(200,200,255)],[1000,"v",10],[2000,"cps",3],[100,"end"]]
boost_zbeub=[[7500,"spider"],[10,"cperso",(255,100,100)],[2000,"v",8],[10,"v",3],[1500,"cperso",(155,155,100)],[10,"v",20],[800,"cperso",(255,0,0)],[100,"end"]]#,[10,(255,200,200)]
boost_essaie = [[1, "arrow"],[10,"v",6],[1,"cperso",(255,155,0)],[100, (20,20,0)],[500,"dr","In my mind",100,200],[350,"dr","In my heart    ",100,200],[600,"dr","This is were we all came from",10,3],[80,"dr","     The dream we have         ",0,3],[1,"spider"],[150,(200,200,200)],[1,"cperso",(255,50,50)],[1,(100,100,255)],[300,"dr","    The love we share     ",0,3],[300,"dr","    This what we're waiting for  ",0,2],[60,"v",3],[600,"dr","and in my mind",20,20],[600,"dr","in my head",40,40],[1100,"dr","This is where we all came from",15,100],[1,"dr","                                   ",15,100],[1,"end"]]
def play(platforms,boost,v,cps):#,pup,text):
  c_perso=(150,150,100)
  fond=(255,)*3
  if platforms[0][0]==500:
    cps=2
    mode="arrow"
  y=100
  loose=0
  s=1
  yy=0
  x=100
  j=1
  to=0
  du=0
  score=0
  fill_rect(0,0,320,222,fond)
  while True:
    fill_rect(0,0,320,1,(50,50,50))
    fill_rect(0,221,320,1,(50,50,50))
    for i in range(len(platforms)):
      platforms[i][0]-=v
      try :
        boost[du][0]-=1
        if boost[du][0]<=0:
          du+=1
        if boost[du][1]=="v":
          v=boost[du][2]
        if boost[du][1]=="cps":
          cps=boost[du][2]
        if boost[du][1]=="arrow":
          mode="arrow"
        if boost[du][1]=="spider":
          mode="spider"
        if type(boost[du][1])==tuple:
          if mode!="spider":
            fill_rect(0,1,320,220,boost[du][1])
            fond=boost[du][1]
        if boost[du][1]=="dr":
            draw_string(boost[du][2],boost[du][3],boost[du][4],c_perso,fond)
        if boost[du][1]=="dr2":
            draw_string(boost[du][2],boost[du][3],boost[du][4],boost[du][5],boost[du][6])
        if boost[du][1]=="adr":
          draw_string(boost[du][2]-v,boost[du][3],c_perso,boost[du][4])
        if boost[du][1]=="cperso":
          c_perso=boost[du][2]
        if boost[du][1]=="end":
          while True:
            x+=1
            fill_rect(x,y,10,10,c_perso)
            fill_rect(x-1,y,1,10,fond)
            draw_string("Vous avez gagne",100,100,c_perso,fond)
            sleep(0.01)
            if x==400:
              break
          homepage_lvl()
      except:
        du+=1
      score+=1
      fill_rect(platforms[i][0],platforms[i][1],platforms[i][2],20,(50,50,50) if platforms[i][3]==0 else (255,0,0))
      fill_rect(platforms[i][0],platforms[i][1],platforms[i][2],20,(50,50,50) if platforms[i][3]==0 else (255,0,0))
      fill_rect(platforms[i][0] + platforms[i][2] ,platforms[i][1],platforms[i][2],20,fond)
      fill_rect(x,y,10,10,c_perso)
      pdev=get_pixel(x+11,y+5)
      pbas=get_pixel(x+10,y+10)
      phau=get_pixel(x+10,y-1)
      if x<=0:
        fill_rect(0,0,320,222,(155,40,40))
        draw_string("GAME OVER",100,100,(0,)*3,(155,40,40))
        sleep(1000)
      if mode=="arrow" and score%cps==0:
        if pbas==(248,0,0) or pdev==(248,0,0) or phau==(248,0,0):
          loose=1
        if pdev==(48,48,48):
          loose=1
        if phau ==(48, 48, 48) or pbas==(48, 48, 48):
          loose=1
        else:
          if keydown(KEY_OK):
            y+=1
            fill_rect(x,y,10,10,c_perso)
            fill_rect(x,y-11,10,10,fond)
          else:
            y-=1
            fill_rect(x,y,10,10,c_perso)
            fill_rect(x,y+11,10,10,fond)
      
      elif (mode=="spider" or mode=="hexa"):
        if pbas==(248,0,0) or pdev==(248,0,0) or phau==(248,0,0):
          x=0
        if pdev==(48,48,48):
          x-=v
        if score%100==0 and keydown(KEY_OK) and s==1 and pbas==(48,48,48) and "spider"==mode:
          while phau!=(48,48,48):
            y-=1
            fill_rect(x,y,10,1,c_perso)
            fill_rect(x,y+10,10,1,fond)
            phau=get_pixel(x,y-1)
          s=0
        if s==1 and pbas!=(48,48,48):
          fill_rect(x,y,10,10,fond)
          if yy<=1:
            yy+=0.5
          if yy==1:
            y+=int(yy)
            yy=0
          fill_rect(x,y,10,10,c_perso)
        if s==0 and phau!=(48,48,48):
          fill_rect(x,y,10,1,c_perso)
          fill_rect(x,y+10,10,1,fond)
          if yy<=1:
            yy+=0.5
          if yy==1:
            y-=int(yy)
            yy=0
        if s==0 and phau!=(48,48,48) and to==0:
          fill_rect(x,y,10,1,c_perso)
          fill_rect(x,y+10,10,1,fond)
          if yy<=1:
            yy+=0.5
          if yy==1:
            y-=int(yy)
            yy=0
        if score%100==0 and keydown(KEY_OK) and s==0 and phau==(48,48,48) and "spider"==mode:
          while pbas!=(48,48,48):
            y+=1
            fill_rect(x,y,10,10,c_perso)
            fill_rect(x,y,10,1,fond)
            pbas=get_pixel(x,y+10)
            s=1

      if loose==1:
        eee=0
        draw_string("game over",110,90,(0,)*3,fond)
        draw_string("EXE : rejouer",80,120,(0,)*3,fond)
        while eee==0:
          sleep(0.05)
          if keydown(KEY_EXE):
            yy=1
            y=100
            x-=v*2
            for i in range(len(platforms)):
              platforms[i][0]+=100
            boost[du][0]+=100
            score=0
            loose=0
            s=1
            fill_rect(0,2,320,219,fond)
            break

lvl =[
  ["1:bourasque",platforms_cmon,boost_cmon,2,2],
  ["2:Zbeub",platforms_zbeub,boost_zbeub,2,2],
  ["3:OOf",platforms_oof,boost_oof,2,2],
  ["4:Essaie",platforms_essaie,boost_essaie,2,2]
  ]
  
  
def homepage_lvl():
  rep=10
  fill_rect(0,0,320,222,(250,250,255))
  draw_string("GD_switch",100,3,(255,)*3,(255,0,0))
  for i in range(len(lvl)):
    draw_string(lvl[i][0],20,50+i*25,(50,)*3,(250,250,100))
  while True:
    if keydown(KEY_ONE):
      rep=0
    elif keydown(KEY_TWO):
      rep=1
    elif keydown(KEY_THREE):
      rep=2
    elif keydown(KEY_FOUR):
      rep=3
    elif keydown(KEY_FIVE):
      rep=4
    elif keydown(KEY_SIX):
      rep=5
    if rep==0 or rep==1 or rep==2 or rep==3 or rep==4 or rep==5:
      loose=1
      play(lvl[rep][1],lvl[rep][2],lvl[rep][3],lvl[rep][4])
homepage_lvl()
