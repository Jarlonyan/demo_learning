export PYTHONPATH=$PATHONPATH:.

# 两种调用方式
# 1.
luigi --module=hello_luigi SquaredNumbers --local-scheduler

# 2.
#python hello_luigi.py SquaredNumbers --local-scheduler --n 20

