datas = {
  "vers": 0.01,
  "config": {
    "rate": "perhr",
    "valueColumns": [
      "vCPU",
      "ECU",
      "memoryGiB",
      "storageGB",
      "linux"
    ],
    "currencies": [
      "USD"
    ],
    "regions": [
      {
        "region": "us-east",
        "instanceTypes": [
          {
            "type": "generalCurrentGen",
            "sizes": [
              {
                "size": "m3.medium",
                "vCPU": "1",
                "ECU": "3",
                "memoryGiB": "3.75",
                "storageGB": "1 x 4 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.070"
                    }
                  }
                ]
              },
              {
                "size": "m3.large",
                "vCPU": "2",
                "ECU": "6.5",
                "memoryGiB": "7.5",
                "storageGB": "1 x 32 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.140"
                    }
                  }
                ]
              },
              {
                "size": "m3.xlarge",
                "vCPU": "4",
                "ECU": "13",
                "memoryGiB": "15",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.280"
                    }
                  }
                ]
              },
              {
                "size": "m3.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "30",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.560"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "computeCurrentGen",
            "sizes": [
              {
                "size": "c3.large",
                "vCPU": "2",
                "ECU": "7",
                "memoryGiB": "3.75",
                "storageGB": "2 x 16 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.105"
                    }
                  }
                ]
              },
              {
                "size": "c3.xlarge",
                "vCPU": "4",
                "ECU": "14",
                "memoryGiB": "7.5",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.210"
                    }
                  }
                ]
              },
              {
                "size": "c3.2xlarge",
                "vCPU": "8",
                "ECU": "28",
                "memoryGiB": "15",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.420"
                    }
                  }
                ]
              },
              {
                "size": "c3.4xlarge",
                "vCPU": "16",
                "ECU": "55",
                "memoryGiB": "30",
                "storageGB": "2 x 160 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.840"
                    }
                  }
                ]
              },
              {
                "size": "c3.8xlarge",
                "vCPU": "32",
                "ECU": "108",
                "memoryGiB": "60",
                "storageGB": "2 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.680"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "gpuCurrentGen",
            "sizes": [
              {
                "size": "g2.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "15",
                "storageGB": "60 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.650"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "hiMemCurrentGen",
            "sizes": [
              {
                "size": "r3.large",
                "vCPU": "2",
                "ECU": "6.5",
                "memoryGiB": "15",
                "storageGB": "1 x 32 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.175"
                    }
                  }
                ]
              },
              {
                "size": "r3.xlarge",
                "vCPU": "4",
                "ECU": "13",
                "memoryGiB": "30.5",
                "storageGB": "1 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.350"
                    }
                  }
                ]
              },
              {
                "size": "r3.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "61",
                "storageGB": "1 x 160 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.700"
                    }
                  }
                ]
              },
              {
                "size": "r3.4xlarge",
                "vCPU": "16",
                "ECU": "52",
                "memoryGiB": "122",
                "storageGB": "1 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.400"
                    }
                  }
                ]
              },
              {
                "size": "r3.8xlarge",
                "vCPU": "32",
                "ECU": "104",
                "memoryGiB": "244",
                "storageGB": "2 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "2.800"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "storageCurrentGen",
            "sizes": [
              {
                "size": "i2.xlarge",
                "vCPU": "4",
                "ECU": "14",
                "memoryGiB": "30.5",
                "storageGB": "1 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.853"
                    }
                  }
                ]
              },
              {
                "size": "i2.2xlarge",
                "vCPU": "8",
                "ECU": "27",
                "memoryGiB": "61",
                "storageGB": "2 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.705"
                    }
                  }
                ]
              },
              {
                "size": "i2.4xlarge",
                "vCPU": "16",
                "ECU": "53",
                "memoryGiB": "122",
                "storageGB": "4 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "3.410"
                    }
                  }
                ]
              },
              {
                "size": "i2.8xlarge",
                "vCPU": "32",
                "ECU": "104",
                "memoryGiB": "244",
                "storageGB": "8 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "6.820"
                    }
                  }
                ]
              },
              {
                "size": "hs1.8xlarge",
                "vCPU": "16",
                "ECU": "35",
                "memoryGiB": "117",
                "storageGB": "24 x 2048",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "4.600"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "Micro and Small Instances",
            "sizes": [
              {
                "size": "t1.micro",
                "vCPU": "1",
                "ECU": "variable",
                "memoryGiB": "0.615",
                "storageGB": "ebsonly",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.020"
                    }
                  }
                ]
              },
              {
                "size": "m1.small",
                "vCPU": "1",
                "ECU": "1",
                "memoryGiB": "1.7",
                "storageGB": "1 x 160",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.044"
                    }
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "region": "us-west-2",
        "instanceTypes": [
          {
            "type": "generalCurrentGen",
            "sizes": [
              {
                "size": "m3.medium",
                "vCPU": "1",
                "ECU": "3",
                "memoryGiB": "3.75",
                "storageGB": "1 x 4 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.070"
                    }
                  }
                ]
              },
              {
                "size": "m3.large",
                "vCPU": "2",
                "ECU": "6.5",
                "memoryGiB": "7.5",
                "storageGB": "1 x 32 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.140"
                    }
                  }
                ]
              },
              {
                "size": "m3.xlarge",
                "vCPU": "4",
                "ECU": "13",
                "memoryGiB": "15",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.280"
                    }
                  }
                ]
              },
              {
                "size": "m3.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "30",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.560"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "computeCurrentGen",
            "sizes": [
              {
                "size": "c3.large",
                "vCPU": "2",
                "ECU": "7",
                "memoryGiB": "3.75",
                "storageGB": "2 x 16 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.105"
                    }
                  }
                ]
              },
              {
                "size": "c3.xlarge",
                "vCPU": "4",
                "ECU": "14",
                "memoryGiB": "7.5",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.210"
                    }
                  }
                ]
              },
              {
                "size": "c3.2xlarge",
                "vCPU": "8",
                "ECU": "28",
                "memoryGiB": "15",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.420"
                    }
                  }
                ]
              },
              {
                "size": "c3.4xlarge",
                "vCPU": "16",
                "ECU": "55",
                "memoryGiB": "30",
                "storageGB": "2 x 160 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.840"
                    }
                  }
                ]
              },
              {
                "size": "c3.8xlarge",
                "vCPU": "32",
                "ECU": "108",
                "memoryGiB": "60",
                "storageGB": "2 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.680"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "gpuCurrentGen",
            "sizes": [
              {
                "size": "g2.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "15",
                "storageGB": "60 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.650"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "hiMemCurrentGen",
            "sizes": [
              {
                "size": "r3.large",
                "vCPU": "2",
                "ECU": "6.5",
                "memoryGiB": "15",
                "storageGB": "1 x 32 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.175"
                    }
                  }
                ]
              },
              {
                "size": "r3.xlarge",
                "vCPU": "4",
                "ECU": "13",
                "memoryGiB": "30.5",
                "storageGB": "1 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.350"
                    }
                  }
                ]
              },
              {
                "size": "r3.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "61",
                "storageGB": "1 x 160 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.700"
                    }
                  }
                ]
              },
              {
                "size": "r3.4xlarge",
                "vCPU": "16",
                "ECU": "52",
                "memoryGiB": "122",
                "storageGB": "1 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.400"
                    }
                  }
                ]
              },
              {
                "size": "r3.8xlarge",
                "vCPU": "32",
                "ECU": "104",
                "memoryGiB": "244",
                "storageGB": "2 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "2.800"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "storageCurrentGen",
            "sizes": [
              {
                "size": "i2.xlarge",
                "vCPU": "4",
                "ECU": "14",
                "memoryGiB": "30.5",
                "storageGB": "1 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.853"
                    }
                  }
                ]
              },
              {
                "size": "i2.2xlarge",
                "vCPU": "8",
                "ECU": "27",
                "memoryGiB": "61",
                "storageGB": "2 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.705"
                    }
                  }
                ]
              },
              {
                "size": "i2.4xlarge",
                "vCPU": "16",
                "ECU": "53",
                "memoryGiB": "122",
                "storageGB": "4 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "3.410"
                    }
                  }
                ]
              },
              {
                "size": "i2.8xlarge",
                "vCPU": "32",
                "ECU": "104",
                "memoryGiB": "244",
                "storageGB": "8 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "6.820"
                    }
                  }
                ]
              },
              {
                "size": "hs1.8xlarge",
                "vCPU": "16",
                "ECU": "35",
                "memoryGiB": "117",
                "storageGB": "24 x 2048",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "4.600"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "Micro and Small Instances",
            "sizes": [
              {
                "size": "t1.micro",
                "vCPU": "1",
                "ECU": "variable",
                "memoryGiB": "0.615",
                "storageGB": "ebsonly",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.020"
                    }
                  }
                ]
              },
              {
                "size": "m1.small",
                "vCPU": "1",
                "ECU": "1",
                "memoryGiB": "1.7",
                "storageGB": "1 x 160",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.044"
                    }
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "region": "us-west",
        "instanceTypes": [
          {
            "type": "generalCurrentGen",
            "sizes": [
              {
                "size": "m3.medium",
                "vCPU": "1",
                "ECU": "3",
                "memoryGiB": "3.75",
                "storageGB": "1 x 4 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.077"
                    }
                  }
                ]
              },
              {
                "size": "m3.large",
                "vCPU": "2",
                "ECU": "6.5",
                "memoryGiB": "7.5",
                "storageGB": "1 x 32 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.154"
                    }
                  }
                ]
              },
              {
                "size": "m3.xlarge",
                "vCPU": "4",
                "ECU": "13",
                "memoryGiB": "15",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.308"
                    }
                  }
                ]
              },
              {
                "size": "m3.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "30",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.616"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "computeCurrentGen",
            "sizes": [
              {
                "size": "c3.large",
                "vCPU": "2",
                "ECU": "7",
                "memoryGiB": "3.75",
                "storageGB": "2 x 16 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.120"
                    }
                  }
                ]
              },
              {
                "size": "c3.xlarge",
                "vCPU": "4",
                "ECU": "14",
                "memoryGiB": "7.5",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.239"
                    }
                  }
                ]
              },
              {
                "size": "c3.2xlarge",
                "vCPU": "8",
                "ECU": "28",
                "memoryGiB": "15",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.478"
                    }
                  }
                ]
              },
              {
                "size": "c3.4xlarge",
                "vCPU": "16",
                "ECU": "55",
                "memoryGiB": "30",
                "storageGB": "2 x 160 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.956"
                    }
                  }
                ]
              },
              {
                "size": "c3.8xlarge",
                "vCPU": "32",
                "ECU": "108",
                "memoryGiB": "60",
                "storageGB": "2 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.912"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "gpuCurrentGen",
            "sizes": [
              {
                "size": "g2.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "15",
                "storageGB": "60 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.702"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "hiMemCurrentGen",
            "sizes": [
              {
                "size": "r3.large",
                "vCPU": "2",
                "ECU": "6.5",
                "memoryGiB": "15",
                "storageGB": "1 x 32 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.195"
                    }
                  }
                ]
              },
              {
                "size": "r3.xlarge",
                "vCPU": "4",
                "ECU": "13",
                "memoryGiB": "30.5",
                "storageGB": "1 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.390"
                    }
                  }
                ]
              },
              {
                "size": "r3.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "61",
                "storageGB": "1 x 160 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.780"
                    }
                  }
                ]
              },
              {
                "size": "r3.4xlarge",
                "vCPU": "16",
                "ECU": "52",
                "memoryGiB": "122",
                "storageGB": "1 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.560"
                    }
                  }
                ]
              },
              {
                "size": "r3.8xlarge",
                "vCPU": "32",
                "ECU": "104",
                "memoryGiB": "244",
                "storageGB": "2 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "3.120"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "storageCurrentGen",
            "sizes": [
              {
                "size": "i2.xlarge",
                "vCPU": "4",
                "ECU": "14",
                "memoryGiB": "30.5",
                "storageGB": "1 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.938"
                    }
                  }
                ]
              },
              {
                "size": "i2.2xlarge",
                "vCPU": "8",
                "ECU": "27",
                "memoryGiB": "61",
                "storageGB": "2 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.876"
                    }
                  }
                ]
              },
              {
                "size": "i2.4xlarge",
                "vCPU": "16",
                "ECU": "53",
                "memoryGiB": "122",
                "storageGB": "4 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "3.751"
                    }
                  }
                ]
              },
              {
                "size": "i2.8xlarge",
                "vCPU": "32",
                "ECU": "104",
                "memoryGiB": "244",
                "storageGB": "8 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "7.502"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "Micro and Small Instances",
            "sizes": [
              {
                "size": "t1.micro",
                "vCPU": "1",
                "ECU": "variable",
                "memoryGiB": "0.615",
                "storageGB": "ebsonly",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.025"
                    }
                  }
                ]
              },
              {
                "size": "m1.small",
                "vCPU": "1",
                "ECU": "1",
                "memoryGiB": "1.7",
                "storageGB": "1 x 160",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.047"
                    }
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "region": "eu-ireland",
        "instanceTypes": [
          {
            "type": "generalCurrentGen",
            "sizes": [
              {
                "size": "m3.medium",
                "vCPU": "1",
                "ECU": "3",
                "memoryGiB": "3.75",
                "storageGB": "1 x 4 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.077"
                    }
                  }
                ]
              },
              {
                "size": "m3.large",
                "vCPU": "2",
                "ECU": "6.5",
                "memoryGiB": "7.5",
                "storageGB": "1 x 32 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.154"
                    }
                  }
                ]
              },
              {
                "size": "m3.xlarge",
                "vCPU": "4",
                "ECU": "13",
                "memoryGiB": "15",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.308"
                    }
                  }
                ]
              },
              {
                "size": "m3.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "30",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.616"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "computeCurrentGen",
            "sizes": [
              {
                "size": "c3.large",
                "vCPU": "2",
                "ECU": "7",
                "memoryGiB": "3.75",
                "storageGB": "2 x 16 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.120"
                    }
                  }
                ]
              },
              {
                "size": "c3.xlarge",
                "vCPU": "4",
                "ECU": "14",
                "memoryGiB": "7.5",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.239"
                    }
                  }
                ]
              },
              {
                "size": "c3.2xlarge",
                "vCPU": "8",
                "ECU": "28",
                "memoryGiB": "15",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.478"
                    }
                  }
                ]
              },
              {
                "size": "c3.4xlarge",
                "vCPU": "16",
                "ECU": "55",
                "memoryGiB": "30",
                "storageGB": "2 x 160 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.956"
                    }
                  }
                ]
              },
              {
                "size": "c3.8xlarge",
                "vCPU": "32",
                "ECU": "108",
                "memoryGiB": "60",
                "storageGB": "2 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.912"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "gpuCurrentGen",
            "sizes": [
              {
                "size": "g2.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "15",
                "storageGB": "60 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.702"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "hiMemCurrentGen",
            "sizes": [
              {
                "size": "r3.large",
                "vCPU": "2",
                "ECU": "6.5",
                "memoryGiB": "15",
                "storageGB": "1 x 32 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.195"
                    }
                  }
                ]
              },
              {
                "size": "r3.xlarge",
                "vCPU": "4",
                "ECU": "13",
                "memoryGiB": "30.5",
                "storageGB": "1 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.390"
                    }
                  }
                ]
              },
              {
                "size": "r3.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "61",
                "storageGB": "1 x 160 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.780"
                    }
                  }
                ]
              },
              {
                "size": "r3.4xlarge",
                "vCPU": "16",
                "ECU": "52",
                "memoryGiB": "122",
                "storageGB": "1 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.560"
                    }
                  }
                ]
              },
              {
                "size": "r3.8xlarge",
                "vCPU": "32",
                "ECU": "104",
                "memoryGiB": "244",
                "storageGB": "2 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "3.120"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "storageCurrentGen",
            "sizes": [
              {
                "size": "i2.xlarge",
                "vCPU": "4",
                "ECU": "14",
                "memoryGiB": "30.5",
                "storageGB": "1 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.938"
                    }
                  }
                ]
              },
              {
                "size": "i2.2xlarge",
                "vCPU": "8",
                "ECU": "27",
                "memoryGiB": "61",
                "storageGB": "2 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.876"
                    }
                  }
                ]
              },
              {
                "size": "i2.4xlarge",
                "vCPU": "16",
                "ECU": "53",
                "memoryGiB": "122",
                "storageGB": "4 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "3.751"
                    }
                  }
                ]
              },
              {
                "size": "i2.8xlarge",
                "vCPU": "32",
                "ECU": "104",
                "memoryGiB": "244",
                "storageGB": "8 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "7.502"
                    }
                  }
                ]
              },
              {
                "size": "hs1.8xlarge",
                "vCPU": "16",
                "ECU": "35",
                "memoryGiB": "117",
                "storageGB": "24 x 2048",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "4.900"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "Micro and Small Instances",
            "sizes": [
              {
                "size": "t1.micro",
                "vCPU": "1",
                "ECU": "variable",
                "memoryGiB": "0.615",
                "storageGB": "ebsonly",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.020"
                    }
                  }
                ]
              },
              {
                "size": "m1.small",
                "vCPU": "1",
                "ECU": "1",
                "memoryGiB": "1.7",
                "storageGB": "1 x 160",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.047"
                    }
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "region": "apac-sin",
        "instanceTypes": [
          {
            "type": "generalCurrentGen",
            "sizes": [
              {
                "size": "m3.medium",
                "vCPU": "1",
                "ECU": "3",
                "memoryGiB": "3.75",
                "storageGB": "1 x 4 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.098"
                    }
                  }
                ]
              },
              {
                "size": "m3.large",
                "vCPU": "2",
                "ECU": "6.5",
                "memoryGiB": "7.5",
                "storageGB": "1 x 32 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.196"
                    }
                  }
                ]
              },
              {
                "size": "m3.xlarge",
                "vCPU": "4",
                "ECU": "13",
                "memoryGiB": "15",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.392"
                    }
                  }
                ]
              },
              {
                "size": "m3.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "30",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.784"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "computeCurrentGen",
            "sizes": [
              {
                "size": "c3.large",
                "vCPU": "2",
                "ECU": "7",
                "memoryGiB": "3.75",
                "storageGB": "2 x 16 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.132"
                    }
                  }
                ]
              },
              {
                "size": "c3.xlarge",
                "vCPU": "4",
                "ECU": "14",
                "memoryGiB": "7.5",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.265"
                    }
                  }
                ]
              },
              {
                "size": "c3.2xlarge",
                "vCPU": "8",
                "ECU": "28",
                "memoryGiB": "15",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.529"
                    }
                  }
                ]
              },
              {
                "size": "c3.4xlarge",
                "vCPU": "16",
                "ECU": "55",
                "memoryGiB": "30",
                "storageGB": "2 x 160 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.058"
                    }
                  }
                ]
              },
              {
                "size": "c3.8xlarge",
                "vCPU": "32",
                "ECU": "108",
                "memoryGiB": "60",
                "storageGB": "2 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "2.117"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "gpuCurrentGen",
            "sizes": [
              {
                "size": "g2.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "15",
                "storageGB": "60 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.000"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "hiMemCurrentGen",
            "sizes": [
              {
                "size": "r3.large",
                "vCPU": "2",
                "ECU": "6.5",
                "memoryGiB": "15",
                "storageGB": "1 x 32 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.210"
                    }
                  }
                ]
              },
              {
                "size": "r3.xlarge",
                "vCPU": "4",
                "ECU": "13",
                "memoryGiB": "30.5",
                "storageGB": "1 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.420"
                    }
                  }
                ]
              },
              {
                "size": "r3.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "61",
                "storageGB": "1 x 160 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.840"
                    }
                  }
                ]
              },
              {
                "size": "r3.4xlarge",
                "vCPU": "16",
                "ECU": "52",
                "memoryGiB": "122",
                "storageGB": "1 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.680"
                    }
                  }
                ]
              },
              {
                "size": "r3.8xlarge",
                "vCPU": "32",
                "ECU": "104",
                "memoryGiB": "244",
                "storageGB": "2 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "3.360"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "storageCurrentGen",
            "sizes": [
              {
                "size": "i2.xlarge",
                "vCPU": "4",
                "ECU": "14",
                "memoryGiB": "30.5",
                "storageGB": "1 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.018"
                    }
                  }
                ]
              },
              {
                "size": "i2.2xlarge",
                "vCPU": "8",
                "ECU": "27",
                "memoryGiB": "61",
                "storageGB": "2 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "2.035"
                    }
                  }
                ]
              },
              {
                "size": "i2.4xlarge",
                "vCPU": "16",
                "ECU": "53",
                "memoryGiB": "122",
                "storageGB": "4 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "4.070"
                    }
                  }
                ]
              },
              {
                "size": "i2.8xlarge",
                "vCPU": "32",
                "ECU": "104",
                "memoryGiB": "244",
                "storageGB": "8 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "8.140"
                    }
                  }
                ]
              },
              {
                "size": "hs1.8xlarge",
                "vCPU": "16",
                "ECU": "35",
                "memoryGiB": "117",
                "storageGB": "24 x 2048",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "5.570"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "Micro and Small Instances",
            "sizes": [
              {
                "size": "t1.micro",
                "vCPU": "1",
                "ECU": "variable",
                "memoryGiB": "0.615",
                "storageGB": "ebsonly",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.020"
                    }
                  }
                ]
              },
              {
                "size": "m1.small",
                "vCPU": "1",
                "ECU": "1",
                "memoryGiB": "1.7",
                "storageGB": "1 x 160",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.058"
                    }
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "region": "apac-tokyo",
        "instanceTypes": [
          {
            "type": "generalCurrentGen",
            "sizes": [
              {
                "size": "m3.medium",
                "vCPU": "1",
                "ECU": "3",
                "memoryGiB": "3.75",
                "storageGB": "1 x 4 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.101"
                    }
                  }
                ]
              },
              {
                "size": "m3.large",
                "vCPU": "2",
                "ECU": "6.5",
                "memoryGiB": "7.5",
                "storageGB": "1 x 32 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.203"
                    }
                  }
                ]
              },
              {
                "size": "m3.xlarge",
                "vCPU": "4",
                "ECU": "13",
                "memoryGiB": "15",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.405"
                    }
                  }
                ]
              },
              {
                "size": "m3.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "30",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.810"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "computeCurrentGen",
            "sizes": [
              {
                "size": "c3.large",
                "vCPU": "2",
                "ECU": "7",
                "memoryGiB": "3.75",
                "storageGB": "2 x 16 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.128"
                    }
                  }
                ]
              },
              {
                "size": "c3.xlarge",
                "vCPU": "4",
                "ECU": "14",
                "memoryGiB": "7.5",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.255"
                    }
                  }
                ]
              },
              {
                "size": "c3.2xlarge",
                "vCPU": "8",
                "ECU": "28",
                "memoryGiB": "15",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.511"
                    }
                  }
                ]
              },
              {
                "size": "c3.4xlarge",
                "vCPU": "16",
                "ECU": "55",
                "memoryGiB": "30",
                "storageGB": "2 x 160 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.021"
                    }
                  }
                ]
              },
              {
                "size": "c3.8xlarge",
                "vCPU": "32",
                "ECU": "108",
                "memoryGiB": "60",
                "storageGB": "2 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "2.043"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "gpuCurrentGen",
            "sizes": [
              {
                "size": "g2.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "15",
                "storageGB": "60 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.898"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "hiMemCurrentGen",
            "sizes": [
              {
                "size": "r3.large",
                "vCPU": "2",
                "ECU": "6.5",
                "memoryGiB": "15",
                "storageGB": "1 x 32 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.210"
                    }
                  }
                ]
              },
              {
                "size": "r3.xlarge",
                "vCPU": "4",
                "ECU": "13",
                "memoryGiB": "30.5",
                "storageGB": "1 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.420"
                    }
                  }
                ]
              },
              {
                "size": "r3.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "61",
                "storageGB": "1 x 160 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.840"
                    }
                  }
                ]
              },
              {
                "size": "r3.4xlarge",
                "vCPU": "16",
                "ECU": "52",
                "memoryGiB": "122",
                "storageGB": "1 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.680"
                    }
                  }
                ]
              },
              {
                "size": "r3.8xlarge",
                "vCPU": "32",
                "ECU": "104",
                "memoryGiB": "244",
                "storageGB": "2 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "3.360"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "storageCurrentGen",
            "sizes": [
              {
                "size": "i2.xlarge",
                "vCPU": "4",
                "ECU": "14",
                "memoryGiB": "30.5",
                "storageGB": "1 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.001"
                    }
                  }
                ]
              },
              {
                "size": "i2.2xlarge",
                "vCPU": "8",
                "ECU": "27",
                "memoryGiB": "61",
                "storageGB": "2 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "2.001"
                    }
                  }
                ]
              },
              {
                "size": "i2.4xlarge",
                "vCPU": "16",
                "ECU": "53",
                "memoryGiB": "122",
                "storageGB": "4 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "4.002"
                    }
                  }
                ]
              },
              {
                "size": "i2.8xlarge",
                "vCPU": "32",
                "ECU": "104",
                "memoryGiB": "244",
                "storageGB": "8 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "8.004"
                    }
                  }
                ]
              },
              {
                "size": "hs1.8xlarge",
                "vCPU": "16",
                "ECU": "35",
                "memoryGiB": "117",
                "storageGB": "24 x 2048",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "5.400"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "Micro and Small Instances",
            "sizes": [
              {
                "size": "t1.micro",
                "vCPU": "1",
                "ECU": "variable",
                "memoryGiB": "0.615",
                "storageGB": "ebsonly",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.026"
                    }
                  }
                ]
              },
              {
                "size": "m1.small",
                "vCPU": "1",
                "ECU": "1",
                "memoryGiB": "1.7",
                "storageGB": "1 x 160",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.061"
                    }
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "region": "apac-syd",
        "instanceTypes": [
          {
            "type": "generalCurrentGen",
            "sizes": [
              {
                "size": "m3.medium",
                "vCPU": "1",
                "ECU": "3",
                "memoryGiB": "3.75",
                "storageGB": "1 x 4 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.098"
                    }
                  }
                ]
              },
              {
                "size": "m3.large",
                "vCPU": "2",
                "ECU": "6.5",
                "memoryGiB": "7.5",
                "storageGB": "1 x 32 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.196"
                    }
                  }
                ]
              },
              {
                "size": "m3.xlarge",
                "vCPU": "4",
                "ECU": "13",
                "memoryGiB": "15",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.392"
                    }
                  }
                ]
              },
              {
                "size": "m3.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "30",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.784"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "computeCurrentGen",
            "sizes": [
              {
                "size": "c3.large",
                "vCPU": "2",
                "ECU": "7",
                "memoryGiB": "3.75",
                "storageGB": "2 x 16 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.132"
                    }
                  }
                ]
              },
              {
                "size": "c3.xlarge",
                "vCPU": "4",
                "ECU": "14",
                "memoryGiB": "7.5",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.265"
                    }
                  }
                ]
              },
              {
                "size": "c3.2xlarge",
                "vCPU": "8",
                "ECU": "28",
                "memoryGiB": "15",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.529"
                    }
                  }
                ]
              },
              {
                "size": "c3.4xlarge",
                "vCPU": "16",
                "ECU": "55",
                "memoryGiB": "30",
                "storageGB": "2 x 160 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.058"
                    }
                  }
                ]
              },
              {
                "size": "c3.8xlarge",
                "vCPU": "32",
                "ECU": "108",
                "memoryGiB": "60",
                "storageGB": "2 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "2.117"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "gpuCurrentGen",
            "sizes": [
              {
                "size": "g2.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "15",
                "storageGB": "60 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.898"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "hiMemCurrentGen",
            "sizes": [
              {
                "size": "r3.large",
                "vCPU": "2",
                "ECU": "6.5",
                "memoryGiB": "15",
                "storageGB": "1 x 32 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.210"
                    }
                  }
                ]
              },
              {
                "size": "r3.xlarge",
                "vCPU": "4",
                "ECU": "13",
                "memoryGiB": "30.5",
                "storageGB": "1 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.420"
                    }
                  }
                ]
              },
              {
                "size": "r3.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "61",
                "storageGB": "1 x 160 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.840"
                    }
                  }
                ]
              },
              {
                "size": "r3.4xlarge",
                "vCPU": "16",
                "ECU": "52",
                "memoryGiB": "122",
                "storageGB": "1 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.680"
                    }
                  }
                ]
              },
              {
                "size": "r3.8xlarge",
                "vCPU": "32",
                "ECU": "104",
                "memoryGiB": "244",
                "storageGB": "2 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "3.360"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "storageCurrentGen",
            "sizes": [
              {
                "size": "i2.xlarge",
                "vCPU": "4",
                "ECU": "14",
                "memoryGiB": "30.5",
                "storageGB": "1 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.018"
                    }
                  }
                ]
              },
              {
                "size": "i2.2xlarge",
                "vCPU": "8",
                "ECU": "27",
                "memoryGiB": "61",
                "storageGB": "2 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "2.035"
                    }
                  }
                ]
              },
              {
                "size": "i2.4xlarge",
                "vCPU": "16",
                "ECU": "53",
                "memoryGiB": "122",
                "storageGB": "4 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "4.070"
                    }
                  }
                ]
              },
              {
                "size": "i2.8xlarge",
                "vCPU": "32",
                "ECU": "104",
                "memoryGiB": "244",
                "storageGB": "8 x 800 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "8.140"
                    }
                  }
                ]
              },
              {
                "size": "hs1.8xlarge",
                "vCPU": "16",
                "ECU": "35",
                "memoryGiB": "117",
                "storageGB": "24 x 2048",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "5.570"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "Micro and Small Instances",
            "sizes": [
              {
                "size": "t1.micro",
                "vCPU": "1",
                "ECU": "variable",
                "memoryGiB": "0.615",
                "storageGB": "ebsonly",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.020"
                    }
                  }
                ]
              },
              {
                "size": "m1.small",
                "vCPU": "1",
                "ECU": "1",
                "memoryGiB": "1.7",
                "storageGB": "1 x 160",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.058"
                    }
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "region": "sa-east-1",
        "instanceTypes": [
          {
            "type": "generalCurrentGen",
            "sizes": [
              {
                "size": "m3.medium",
                "vCPU": "1",
                "ECU": "3",
                "memoryGiB": "3.75",
                "storageGB": "1 x 4 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.095"
                    }
                  }
                ]
              },
              {
                "size": "m3.large",
                "vCPU": "2",
                "ECU": "6.5",
                "memoryGiB": "7.5",
                "storageGB": "1 x 32 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.190"
                    }
                  }
                ]
              },
              {
                "size": "m3.xlarge",
                "vCPU": "4",
                "ECU": "13",
                "memoryGiB": "15",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.381"
                    }
                  }
                ]
              },
              {
                "size": "m3.2xlarge",
                "vCPU": "8",
                "ECU": "26",
                "memoryGiB": "30",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.761"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "computeCurrentGen",
            "sizes": [
              {
                "size": "c3.large",
                "vCPU": "2",
                "ECU": "7",
                "memoryGiB": "3.75",
                "storageGB": "2 x 16 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.163"
                    }
                  }
                ]
              },
              {
                "size": "c3.xlarge",
                "vCPU": "4",
                "ECU": "14",
                "memoryGiB": "7.5",
                "storageGB": "2 x 40 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.325"
                    }
                  }
                ]
              },
              {
                "size": "c3.2xlarge",
                "vCPU": "8",
                "ECU": "28",
                "memoryGiB": "15",
                "storageGB": "2 x 80 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "0.650"
                    }
                  }
                ]
              },
              {
                "size": "c3.4xlarge",
                "vCPU": "16",
                "ECU": "55",
                "memoryGiB": "30",
                "storageGB": "2 x 160 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "1.300"
                    }
                  }
                ]
              },
              {
                "size": "c3.8xlarge",
                "vCPU": "32",
                "ECU": "108",
                "memoryGiB": "60",
                "storageGB": "2 x 320 SSD",
                "valueColumns": [
                  {
                    "name": "linux",
                    "prices": {
                      "USD": "2.600"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "Micro and Small Instances",
            "sizes": [
              {
                "size": "t1.micro",
                "vCPU": "1",
                "ECU": "variable",
                "memoryGiB": "0.615",
                "storageGB": "ebsonly",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.027"
                    }
                  }
                ]
              },
              {
                "size": "m1.small",
                "vCPU": "1",
                "ECU": "1",
                "memoryGiB": "1.7",
                "storageGB": "1 x 160",
                "valueColumns": [
                  {
                    "name": "os",
                    "prices": {
                      "USD": "0.058"
                    }
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  }
}
