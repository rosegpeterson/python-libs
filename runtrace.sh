echo "trace => "
python -m trace --trace $1.py
echo "deb => "
python -m pdb $1.py
