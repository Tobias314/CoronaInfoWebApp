from webcrawler.googlespreadsheet.googlespreadhsheetcrawler import GoogleSpreadSheetCrawler

def main():
    sheets_crawler = GoogleSpreadSheetCrawler()
    res = sheets_crawler.crawl_spreadsheet('1wg-s4_Lz2Stil6spQEYFdZaBEp8nWW26gVyfHqvcl8s', 'Haupt!A6:A42')
    print(res)

if __name__=='__main__':
    main()