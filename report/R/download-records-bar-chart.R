# library("RColorBrewer") (already loaded by R Studio)

years <- c('2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006')
records <- c(5997, 6789, 5100, 3414, 412, 72, 28, 23, 2)

bp <- barplot(records, main="", names.arg=years, col=brewer.pal(9, "Set1"), 
        xlab="Year", ylab="Number of Sub-Award Records Available", ylim=c(0, 8000))

text(x=bp, y=records, label=records, pos=3, cex=0.8, col="black")