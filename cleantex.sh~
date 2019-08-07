
echo -e " \n Current Directory is : " $PWD

echo -e "\n List of files \n"

ls | egrep '\.aux$|\.bbl$|\.lof$|\.log$|\.lot$|\.gz$|\.toc$|\.pdf$|\.png$|\.blg$\.eps$'

read -p "Confirm deletion (y/n) " choice

if [ "$choice" = "y" ] || [ "$choice" = "Y" ] ;
   then
      echo -e "\n Removing LaTeX generated files \n "
      rm *aux *.bbl *.lof *.log *.lot *.gz *.toc *.pdf *.png *.blg *.eps
      echo -e "\n Files have been deleted \n"
      echo -e "\n Copying the CFDVRi logo to present directory \n"
      cp /home/praphul/Pictures/cfdvri_logo.png $PWD
else 
      echo "Aborting Deletion"
      exit 
fi


