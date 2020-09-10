name := "SparkSQL"

version := "1.0"

organization := "com.alirezamoosavi"

scalaVersion := "2.11.8"

assemblyMergeStrategy in assembly := {
 case PathList("META-INF", xs @ _*) => MergeStrategy.discard
 case x => MergeStrategy.first
}

libraryDependencies ++= Seq(
"org.apache.spark" %% "spark-core" % "2.4.6" % "provided",
"org.apache.spark" %% "spark-sql" % "2.4.6"
)