
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        print(self.datas)

    def output_html(self):
        fout = open('output.html','w',encoding='utf-8')

        fout.write("<html>")
        fout.write("<body>")
        #加入网页编码
        fout.write("<head><meta charset = 'utf-8'></head>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write('<td>{}</td>'.format(data["url"]))
            fout.write('<td>{}</td>'.format(data["title"]))
            fout.write('<td>{}</td>'.format(data["summary"]))
            fout.write("</td>")
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()