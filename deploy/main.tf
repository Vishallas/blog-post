provider "aws" {
  region = "us-east-1"
}

resource "aws_dynamodb_table" "Post" {
  name         = "Post"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "postid"
  attribute {
    name = "postid"
    type = "S"
  }
}

resource "aws_s3_bucket" "post_images" {
  bucket        = "public-post-files-presidio"
  force_destroy = true

}

resource "aws_s3_bucket_public_access_block" "example" {
  bucket = aws_s3_bucket.post_images.id
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_instance" "name" {
  instance_type = "t2.medium"
  security_groups = ["sg-06134a4c3d63c0d0b"]
  key_name = "blogpost"
  ami = "ami-08a0d1e16fc3f61ea"
  tags = {
    Name = "BlogPostBackendServer"
  }
  user_data = "${file("./user_data.sh")}"
  user_data_replace_on_change = true
}