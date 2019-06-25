#!/usr/bin/env ruby

module JsonLib
    class << self; attr_accessor :json_files; end
    self.json_files = [
        "./json_output/2016_2017_1.json", 
        "./json_output/2016_2017_2.json", 
        "./json_output/2016_2017_3.json", 
        "./json_output/2017_2018_1.json", 
        "./json_output/2017_2018_2.json", 
        "./json_output/2017_2018_3.json", 
        "./json_output/2018_2019_1.json", 
        "./json_output/2018_2019_2.json",
        "./json_output/2018_2019_3.json"];
end