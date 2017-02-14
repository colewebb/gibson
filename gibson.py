from glob import glob
from subprocess import call
locations = open("./path.db")
music=[]
for line in locations:
	line=line.rstrip()
	music=music+glob(line+"/*.mp3")
ticker=0
index=open("./html/index.html","w")
index.write("<head><link rel='stylesheet' href='./main.css'><title>Gibson Home</title></head><body><h2>Gibson Home</h2>")
index.close()
for i in music:
	call_line="touch ./html/"+str(ticker)+".html"
	call(call_line,shell=True)
	file=open("./html/"+str(ticker)+".html","w")
	write_line="<head><link rel='stylesheet' href='./player.css'><title>"+str(ticker)+"</title></head><body>"+music[ticker]+"<br><br><audio controls autoplay><source src="+music[ticker]+" type='audio/mpeg'></audio><br><br></body>"
	file.write(write_line)
	if ticker==0:
		page_status="first"
		write_line="Previous | <a href='./index.html'>Home</a> | <a href='./"+str(ticker+1)+".html'>Next</a></body>"
		file.write(write_line)
	elif ticker+1==len(music):
		page_status="last"
		write_line="<a href='"+str(ticker-1)+".html'>Previous</a> | <a href='./index.html'>Home</a> | <div class='grey'>Next</div></body>"
		file.write(write_line)
	else:
		page_status="middle"
		write_line="<a href='"+str(ticker-1)+".html'>Previous</a> | <a href='./index.html'>Home</a> | <a href='./"+str(ticker+1)+".html'>Next</a></body>"
		file.write(write_line)
	file.close()
	index=open("./html/index.html","a")
	write_line="<a href='"+str(ticker)+".html'>"+music[ticker]+"</a><br><br>"
	index.write(write_line)
	ticker=ticker+1
index.write("</body>")
index.close()
call("chromium-browser --app=file:///home/rebooted/scripts/gibson/html/index.html",shell=True)
