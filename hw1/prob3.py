from pylab import *
from matplotlib.backends.backend_pdf import PdfPages

tire_data = open('tire.txt', 'r')

# Two brands
brand_a, brand_b = [],[]

# Go through file, add column 1 to brand_a
# add column 2 to brand_b
for line in tire_data:
    line = line.strip()
    sline = line.split()
    try:
        brand_a.append(float(sline[0]))
        brand_b.append(float(sline[1]))
    except IndexError:
        pass

tire_data.close()


both = [brand_a, brand_b]

pdf = PdfPages('tires.pdf')

figure()
boxplot(both, 0, 'rs', 0)
title('BoxPlot')
savefig(pdf, format='pdf')
close()

figure()
hist(brand_a)
title('Histogram for Brand A')
pdf.savefig()
close()

figure()
hist(brand_b)
title('Histogram for Brand B')
pdf.savefig()
close()

pdf.close()
