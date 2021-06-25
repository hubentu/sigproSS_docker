import sys
import os
from shutil import copy
from sigproSS import spss
import sigProfilerPlotting as plot
import matplotlib.pyplot as plt
plt.switch_backend('agg')

vcf = sys.argv[1]
os.mkdir("results")
copy(vcf, "results/")
spss.single_sample("results", "results", exome=True, ref="GRCh37")
##plot.plotSBS(output+"/Signatures.txt", output+"/Signature_plot", "", "96", True, custom_text_upper= " ")
