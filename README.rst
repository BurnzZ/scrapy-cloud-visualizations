Scrapy Cloud Visualizations
===========================

Ideally, this shall be a great tool for managing and maintaining spiders as it offers some additional way of visualizing some of its key aspects.

Usage
~~~~~

.. code-block:: python
   from scrapy_cloud_visualizer import Visualizer
   viz = Visualizer('APIKEY123', '123456')
   viz.show_heatmap_jobs('my_awesome_spider')

Fix for `matplotlib` problem in Mac OSX 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python
