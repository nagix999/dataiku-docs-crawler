DSS and Hadoop[¶](#dss-and-hadoop "Permalink to this heading")
==============================================================



* [Setting up Hadoop integration](installation.html)
	+ [Prerequisites](installation.html#prerequisites)
		- [Supported distributions](installation.html#supported-distributions)
		- [Non supported distributions](installation.html#non-supported-distributions)
		- [Software install](installation.html#software-install)
		- [HDFS](installation.html#hdfs)
		- [Hive](installation.html#hive)
	+ [Testing Hadoop connnectivity prior to installation](installation.html#testing-hadoop-connnectivity-prior-to-installation)
		- [hive binary](installation.html#hive-binary)
	+ [Setting up DSS Hadoop integration](installation.html#setting-up-dss-hadoop-integration)
		- [Test HDFS connection](installation.html#test-hdfs-connection)
		- [Standalone Hadoop integration](installation.html#standalone-hadoop-integration)
		- [Configure Hive connectivity](installation.html#configure-hive-connectivity)
		- [Configure Impala connectivity](installation.html#configure-impala-connectivity)
	+ [Secure Hadoop connectivity](installation.html#secure-hadoop-connectivity)
* [Connecting to secure clusters](secure-clusters.html)
	+ [Setup the DSS Kerberos account](secure-clusters.html#setup-the-dss-kerberos-account)
	+ [Configure DSS for Hadoop security](secure-clusters.html#configure-dss-for-hadoop-security)
		- [Test HDFS connection](secure-clusters.html#test-hdfs-connection)
		- [Configure Hive connectivity](secure-clusters.html#configure-hive-connectivity)
		- [Configure Impala connectivity](secure-clusters.html#configure-impala-connectivity)
	+ [Modification of principal or keytab](secure-clusters.html#modification-of-principal-or-keytab)
	+ [Advanced settings (optional)](secure-clusters.html#advanced-settings-optional)
		- [Configuring Kerberos credentials periodic renewal](secure-clusters.html#configuring-kerberos-credentials-periodic-renewal)
* [Hadoop filesystems connections (HDFS, S3, EMRFS, WASB, ADLS, GS)](hadoop-fs-connections.html)
	+ [HDFS connections in DSS](hadoop-fs-connections.html#hdfs-connections-in-dss)
		- [Managed datasets setup](hadoop-fs-connections.html#managed-datasets-setup)
	+ [Connecting to the “default” FS](hadoop-fs-connections.html#connecting-to-the-default-fs)
	+ [Connecting to the HDFS of other clusters](hadoop-fs-connections.html#connecting-to-the-hdfs-of-other-clusters)
	+ [Connecting to S3](hadoop-fs-connections.html#connecting-to-s3)
		- [Using S3A](hadoop-fs-connections.html#using-s3a)
		- [Using EMRFS](hadoop-fs-connections.html#using-emrfs)
		- [Using VPC Endpoints](hadoop-fs-connections.html#using-vpc-endpoints)
	+ [Connecting to Azure Blob Storage](hadoop-fs-connections.html#connecting-to-azure-blob-storage)
	+ [Connecting to Google Cloud Storage](hadoop-fs-connections.html#connecting-to-google-cloud-storage)
	+ [Connecting to Azure Data Lake Store (gen1\)](hadoop-fs-connections.html#connecting-to-azure-data-lake-store-gen1)
	+ [Connecting to Azure Data Lake Store (gen2\)](hadoop-fs-connections.html#connecting-to-azure-data-lake-store-gen2)
	+ [Additional details](hadoop-fs-connections.html#additional-details)
		- [Cloud storage credentials](hadoop-fs-connections.html#cloud-storage-credentials)
		- [Checking access to a Hadoop filesystem](hadoop-fs-connections.html#checking-access-to-a-hadoop-filesystem)
		- [Relation to the Hive metastore](hadoop-fs-connections.html#relation-to-the-hive-metastore)
* [Hive](hive.html)
	+ [Interaction with the Hive global metastore](hive.html#interaction-with-the-hive-global-metastore)
	+ [Synchronisation to the Hive metastore](hive.html#synchronisation-to-the-hive-metastore)
		- [For external datasets](hive.html#for-external-datasets)
	+ [Importing from the Hive metastore](hive.html#importing-from-the-hive-metastore)
	+ [Hive execution engines](hive.html#hive-execution-engines)
		- [Notebooks and metrics](hive.html#notebooks-and-metrics)
		- [Recipes](hive.html#recipes)
			* [Hiveserver 2](hive.html#hiveserver-2)
			* [Hive CLI (global metastore)](hive.html#hive-cli-global-metastore)
			* [Hive CLI (isolated metastore)](hive.html#hive-cli-isolated-metastore)
			* [Choosing the mode](hive.html#choosing-the-mode)
			* [Configuring the mode](hive.html#configuring-the-mode)
	+ [Support for Hive authentication modes](hive.html#support-for-hive-authentication-modes)
	+ [Support for Hive authorization modes](hive.html#support-for-hive-authorization-modes)
		- [No Hive security (No DSS User Isolation)](hive.html#no-hive-security-no-dss-user-isolation)
		- [Ranger (No DSS User Isolation)](hive.html#ranger-no-dss-user-isolation)
		- [Ranger (DSS User Isolation enabled)](hive.html#ranger-dss-user-isolation-enabled)
		- [Storage\-based security (No DSS User Isolation)](hive.html#storage-based-security-no-dss-user-isolation)
	+ [Supported file formats](hive.html#supported-file-formats)
		- [Limitations](hive.html#limitations)
	+ [Internal details](hive.html#internal-details)
* [Impala](impala.html)
	+ [Impala connectivity](impala.html#impala-connectivity)
	+ [Metastore synchronization](impala.html#metastore-synchronization)
	+ [Supported formats and limitations](impala.html#supported-formats-and-limitations)
	+ [Configuring connection to Impala servers](impala.html#configuring-connection-to-impala-servers)
		- [Kerberos authentication (secure clusters)](impala.html#kerberos-authentication-secure-clusters)
		- [LDAP authentication](impala.html#ldap-authentication)
	+ [Using Impala to write outputs](impala.html#using-impala-to-write-outputs)
		- [No Hive authorization (DSS regular security)](impala.html#no-hive-authorization-dss-regular-security)
		- [Ranger](impala.html#ranger)
		- [Switching from write\-through\-DSS to write\-through\-Impala](impala.html#switching-from-write-through-dss-to-write-through-impala)
* [Spark](spark.html)
	+ [Verify the installation](spark.html#verify-the-installation)
		- [Additional topics](spark.html#additional-topics)
	+ [Metastore security](spark.html#metastore-security)
	+ [Configure Spark logging](spark.html#configure-spark-logging)
* [Hive datasets](hive-dataset.html)
	+ [Use cases](hive-dataset.html#use-cases)
		- [Hive views](hive-dataset.html#hive-views)
		- [No read access on source files](hive-dataset.html#no-read-access-on-source-files)
		- [ACID tables (ORC)](hive-dataset.html#acid-tables-orc)
		- [DATE and DECIMAL data types](hive-dataset.html#date-and-decimal-data-types)
	+ [Creating a Hive dataset](hive-dataset.html#creating-a-hive-dataset)
		- [New dataset](hive-dataset.html#new-dataset)
		- [Import](hive-dataset.html#import)
	+ [Using a Hive dataset](hive-dataset.html#using-a-hive-dataset)
		- [Hive recipes](hive-dataset.html#hive-recipes)
		- [Visual recipes with Hive as execution engine](hive-dataset.html#visual-recipes-with-hive-as-execution-engine)
		- [Spark recipes](hive-dataset.html#spark-recipes)
		- [Visual recipes with Spark as execution engine](hive-dataset.html#visual-recipes-with-spark-as-execution-engine)
		- [Limitations](hive-dataset.html#limitations)
* [Hadoop user isolation](user-isolation.html)
* [Distribution\-specific notes](distributions/index.html)
	+ [Cloudera CDP](distributions/cdp.html)
		- [Spark support](distributions/cdp.html#spark-support)
		- [Security](distributions/cdp.html#security)
		- [Know issues](distributions/cdp.html#know-issues)
* [Teradata Connector For Hadoop](tdch.html)
	+ [Installation and configuration](tdch.html#installation-and-configuration)
	+ [Usage and Guidelines](tdch.html#usage-and-guidelines)
	+ [Limitations](tdch.html#limitations)
* [Multiple Hadoop clusters](multi-clusters.html)
	+ [Concepts](multi-clusters.html#concepts)
		- [Builtin cluster](multi-clusters.html#builtin-cluster)
		- [Additional clusters](multi-clusters.html#additional-clusters)
		- [Managed dynamic clusters](multi-clusters.html#managed-dynamic-clusters)
		- [Use an additional cluster](multi-clusters.html#use-an-additional-cluster)
			* [Per\-scenario additional clusters](multi-clusters.html#per-scenario-additional-clusters)
	+ [Restrictions](multi-clusters.html#restrictions)
	+ [Define an additional static cluster](multi-clusters.html#define-an-additional-static-cluster)
		- [Hadoop](multi-clusters.html#hadoop)
		- [Hive](multi-clusters.html#hive)
		- [Impala](multi-clusters.html#impala)
		- [Spark](multi-clusters.html#spark)
	+ [Use a specific cluster for scenarios](multi-clusters.html#use-a-specific-cluster-for-scenarios)
	+ [Permissions](multi-clusters.html#permissions)