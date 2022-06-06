# Course-Tutor-Attrition
Analyses and Prediction of Course Tutor Attrition at the University of Cape Coast - Collage of Distance Education (CoDE)

<hr/>

<img src = 'https://www.kindpng.com/picc/m/500-5000015_amazon-s3-bucket-icon-hd-png-download.png' alt = 's3 bucket image' />

This branch of the repository contains the Scripts for automating aws instances

<p> Currently supported actions:</p>
<ul>
 <li> Creating a New Bucket </li>
 <li> Updating Bucket Policies </li>
 <li> Uploading objects </li>
</ul>

<div>

<h2>Usage</h2>


<h3> Creating a bucket </h3> <br/>
$ python aws-config.py --create_bucket --bucket <'globally_unique_bucket_name'>

<em><b> shortcut <b></em><br/> <br/>
$ python aws-config.py -c -b <'globally_unique_bucket_name'>

<h3> Uploading an Object into an S3 bucket </h3><br/>
$ python aws-config.py --upload_file --bucket <'globally_unique_bucket_name'> --object <'object_path'> --filename <'file_name'> 

<em><b> shortcut <b></em><br/><br/>
$ python aws-config.py -u -b <'globally_unique_bucket_name'> -o <object_path> -f <'file_name'> 

<h3> Updating Bucket Policy </h3><br/>
$ python aws-config.py --update_policy --policy_file <'path_to_policy_json_file'>

<em><b> shortcut <b></em><br/> <br/>
$ python aws-config.py -up -p <'path_to_policy_json_file'>
</div>

