#================================================
# Script to compress pdf files via ghostscript
# 
# Date : 26/04/2019
#================================================


# Ebook reduction 

#gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
#       -dNOPAUSE -dBATCH  -dQUIET -sOutputFile=output.pdf input.pdf


#-dPDFSETTINGS=/screen   (screen-view-only quality, 72 dpi images)
#-dPDFSETTINGS=/ebook    (low quality, 150 dpi images)
#-dPDFSETTINGS=/printer  (high quality, 300 dpi images)
#-dPDFSETTINGS=/prepress (high quality, color preserving, 300 dpi imgs)
#-dPDFSETTINGS=/default  (almost identical to /screen)

# Change the output and input file name. 

gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dBATCH  -dQUIET -sOutputFile=ReportCompress.pdf Report.pdf



# Reference 

## 1] http://milan.kupcevic.net/ghostscript-ps-pdf/ 
