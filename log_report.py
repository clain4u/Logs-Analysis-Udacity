#!/usr/bin/env python2
import psycopg2


def main():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()

    # =============== Most popular three articles of all time ================
    print "\nMost popular three articles of all time.\n"
    c.execute("""
              select articles.title as article, views_report.views from
              (select replace(path,'/article/','') slug, count(path) as views
              from log where log.path <> '/' and status='200 OK' group by path
              order by views desc limit 3) views_report join articles on
              views_report.slug=articles.slug order by views_report.views desc
              """)
    rows = c.fetchall()
    for row in rows:
        print row[0] + " - " + str(row[1]) + " views"

    # =============== Most popular article authors of all time ===============
    print "\n\nMost popular article authors of all time.\n"
    c.execute("""
              select authors.name, views_by_authors.total_views from
              (select author as author_id , sum(views) total_views from
              (select * from (select replace(path,'/article/','') slug,
              count(path) as views from log where log.path <> '/' group by path
              order by views desc) views_report join articles on
              views_report.slug = articles.slug) author_view_report
              group by author order by total_views desc ) views_by_authors
              join authors on views_by_authors.author_id = authors.id
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
