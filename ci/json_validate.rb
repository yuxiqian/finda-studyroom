#!/usr/bin/env ruby

require 'rubygems'
require 'json'
require './ci/json_lib'

include JsonLib

counter = 0
total_file_cnt = JsonLib.json_files.length
JsonLib.json_files.each do |f|
    json = File.read(f)
    obj = JSON.parse(json)
    counter += 1
    printf("Valid File (%d/%d): %s\n", counter, total_file_cnt, f)
end