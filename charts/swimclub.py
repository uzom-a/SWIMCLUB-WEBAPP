import statistics
import hfpy_utils

CHARTS = "charts/"

FOLDER = "swimdata/"

def read_swim_data(filename):    
    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")
    with open(FOLDER+filename) as df:
        times = df.readlines()[0].strip().split(",")
    converts=[]
    for t in times:
        if ":" in t:
         minutes, rest = t.split(":")
         seconds, hundredths = rest.split(".")
        else:
           minutes = 0
           seconds, hundredths = t.split(".")
        converts.append(int(minutes)*60*100 +int(seconds)*100 + int(hundredths) )
    average = statistics.mean(converts)
    mins_secs, hundredths = f"{(average / 100):.2f}".split(".")
    mins = int(mins_secs)
    minutes= mins // 60
    second = mins - minutes*60
    average = f"{minutes}:{seconds:0>2}.{hundredths}"
    return swimmer, age, distance, stroke, times, average, converts 

def produce_bar_chart(fn, location=CHARTS):
    #Given the name of a swimmer's file, produce a HTML/SVG-based bar chart and save the chart to the the CHARTS folder and reeturn the bar chart to the bar chart file
    swimmer, age, distance, stroke, times, average, converts = read_swim_data(fn)
    from_max = max(converts)
    times.reverse()
    converts.reverse()
    title = f"{swimmer} (Under {age}) {distance} {stroke}"
    header = f"""<!DOCTYPE html>
                   <html>
                      <head>
                           <title>{title}</title>
                           </head>
                           <body>
                               <h3>{title}</h3>"""
    body=""
    for n, t in enumerate(times):
       bar_width = hfpy_utils.convert2range(converts[n], 0, from_max, 0, 350)
       body= body +f"""
                            <svg height="30" width="400">
                                <rect height="30" width="{bar_width}" style="fill:rgb(0,0,255);" />
                            </svg>{t}<br />"""
       footer = f"""
                     <p>Average time:{average}</p>
                  </body>
               </html>"""
       page = header + body + footer
       save_to = f"{location}{fn.removesuffix('.txt')}.html"
       with open(save_to, "w") as sf:
          print(page, file=sf)

    return save_to      