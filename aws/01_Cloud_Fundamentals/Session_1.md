# Cloud Computing Fundamentals

## Fundamentals

### Capex vs Opex
_Scenario 1_ How should i store my excess data as my system is running out of space

#### **Capital Expense**
- _Option_ Buying a hard drive, One time investment  e.g 1 TB hard drive.
- _Capacity Planning_ to ensure the hard drive does not run out of space and can be used for few years.
- _Maintenance_ will be required for the hard-drive and will have to do it on your own.
- _Investment_ is completely upfront.

#### **Operational Expense**
- _Option_ Getting a google drive or aws s3 or onedrive  
- _Capacity Planning_ Not required as i can change my plan as per my need [ 15 GB free tier to minimal paymment for 100 gb]
- _Maintenance_ none required, this is completely managed by the providers
- _Investment_ Paying as per my utilization, rathen than upfront cost, i am paying as per my utilization.

### Elasticity
Company generates reports of sales on 15th and 30th of every months. Report generation is a computational expensive process which pushes the existing infrastructure to limit and causing a lot of issues. Rest of the month the system is less than 30% utilized.

#### **Elasticity defined**
The ability of a cloud service to provide on-demand offerings, nimbly switching resources when demand goes up or down. In above scenario, additional resources can be added on 15th and 30th, once the processing is completed, the additional resouces can be removed.

- _Advantage_ I am only paying for what i am using and this cannot be done in case of on-prem. Additonal resources on demand.

*In cloud computing, elasticity is defined as “the degree to which a system is able to adapt to workload changes by provisioning and de-provisioning resources in an autonomic manner, such that at each point in time the available resources match the current demand as closely as possible”.*

Additonal Reading

- [Edureka: An Introduction to AWS](https://www.edureka.co/blog/what-is-aws/)
- [Edureka: Cloud Computing Introduction](https://www.edureka.co/blog/amazon-aws-tutorial/)
- [Elasticity and Scalability](https://medium.com/@pablo.iorio/elasticity-does-not-equal-scalability-246bd9b3c128)
- [AWS CLI Installation and Configuration](https://www.edureka.co/blog/how-to-use-aws-cli/)
- [AWS Console: Deep Dive Into AWS Management Interface](https://www.edureka.co/blog/aws-console/)
- [Putty Download](https://www.putty.org/)  
- [Putty using windows](https://linuxacademy.com/guide/17385-use-putty-to-access-ec2-linux-instances-via-ssh-from-windows/)  

**Cloud Service Model**

Report Generation used to happen on 15th and on 30th
On Prem ---> non responsive Add more RAM or storage
Cloud ---> 15th and 30th ----> 2->8

1st to 14th 2 machine
15th ---> 8 machine


when you provision a machine in cloud ---> 

Submit a request saying i need a machine [CPU, RAM, Storage, OS [Machine Image]]  ---> Machine

You submit this request to a specific region


Cost Optimization


if %cpu utilization goes above 70% add a new instance
if %cpu utilization goes below 50% then removed additional instances


Managed and Unmanaged

Managed Database --> SQL Ser {Certain version of MySql5} are expensive

99.99999999
99.99995555

Who has more control
Are you having more control or Amazon has more control

Most of the time
I want to share a file with you

AWS ---> S3 (Simple Storage Service)

Provide you a storage 

Region means ---> I have datacenter in particular places
Mumbai -- Geographicall i have data centers in Geographic location
Regions ---> Avaibility Zone

Mumbai region ---> 4 (data centers)

2 datacenters Mumbai (AZ1) 2 datacenter are in Pune (AZ2)

**SDN (Software Defined Network)**

The resources provided to your are created on demand and they are a logical seperation of a hardware equipment.

**MTTR**

MTTR is calculated by dividing the total downtime caused by failures by the total number of failures. If, for example, a system fails three times in a month, and the failures resulted in a total of six hours of downtime, the MTTR would be two hours.

MTTR = 6 hours / 3 failures = 2 hours

[Key Matrices](https://www.splunk.com/en_us/data-insider/what-is-mean-time-to-repair.html)


Steps to Install AWS CLi

Windows you are going to download 64-32 bit set up.
Mac 
-- pip (Python Installer) aws-cli package
-- python 3.6 version
-- Python path was not in the enviroment variable
-- Hence i was not able to run aws
-- you have to update the profile


Login to a machine - i can create a new pair or use an existing 
Public Private Key Pair ---> *.pem file


EC2 --> Elastic Cloud Compute :)  [Virtual Server] t2.nano t2.micro

Additonal Links  
[Putty Download](https://www.putty.org/)  
[Putty using windows](https://linuxacademy.com/guide/17385-use-putty-to-access-ec2-linux-instances-via-ssh-from-windows/)  







