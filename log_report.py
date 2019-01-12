#!/usr/bin/env python2
import psycopg2


def main():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()

    # =============== Most popular three articles of all time ================
    print "\nMost popular three articles of all time.\n"
    c.execute("""
              select articles.title , count(path) as views
              from log join articles on
              log.path = CONCAT('/article/', articles.slug)
              where log.path <> '/' and status='200 OK' group by
              articles.title, log.path order by views desc limit 3
              """)
    rows = c.fetchall()
    for row in rows:
        print row[0] + " - " + str(row[1]) + " views"

    # =============== Most popular article authors of all time ===============
    print "\n\nMost popular article authors of all time.\n"
    c.execute("""
              select authors.name, sum(author_views.views) as views from(
              select articles.author, count(path) as views
              from log join articles on
              log.path = CONCAT('/article/', articles.slug)
              where log.path <> '/' and status='200 OK' group by
              articles.author, log.path order by views desc) author_views
              join authors on author_views.author = authors.id group by
              authors.name,author_views.author order by views desc
              """)
    rows = c.fetchall()
    for row in rows:
        print row[0] + " - " + str(row[1]) + " views"

    # ============= Days when more than 1% of requests lead to errors =========
    print "\n\nDays when more than 1% of requests lead to errors.\n"
    c.execute("""
              select TO_CHAR(error_views.date,'Mon DD, YYYY') date,
              error_views.error_hits,total_views.hits,
              round(((
              error_views.error_hits::decimal/total_views.hits::decimal
              )*100),2) error_percentage from
              (select time::date as date,count(status) error_hits from log
              where status <> '200 OK' group by date) error_views
              join (select time::date as date,count(status) hits from log
              group by date) total_views on error_views.date = total_views.date
              where((
              error_views.error_hits::decimal/total_views.hits::decimal
              )*100) > 1 order by date asc
              """)
    rows = c.fetchall()
    for row in rows:
        print str(row[0]) + " -- " + str(row[1]) + " error requests  -- ",
        print str(row[2]) + " total requests -- " + str(row[3]) + "% error.\n"

    db.close()


if __name__ == '__main__':
    main()
