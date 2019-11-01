#!/bin/bash
set -e

nextflow \
    -C "nextflow.local.config" \
    run \
    main.nf \
    --dry-run \
    --param1 data/test_in1 \
    --param2 data/test_in2 \
    --param3 data/test_in3 \
    --outdir output \
    -with-report output/nextflow_report.html \
    -work-dir output/work/ \
    -resume \
