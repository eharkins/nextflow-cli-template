#!/usr/bin/python
import click
import subprocess

def run_cmds(cmds, shell=False):
    for cmd in cmds:
        subprocess.check_call(cmd, shell=shell)

def write_cmds_to_file(cmds, fname):
    with open(fname, 'w') as fh:
        for cmd in cmds:
            fh.write(cmd + '\n')

def dry_check_run_cmds(cmds, ctx, outfile=None, shell=False):
    if ctx.obj['DRY']:
        write_cmds_to_file(cmds, outfile)
    else:
        run_cmds(cmds, shell=shell)

@click.group()
@click.option('--dry/--no-dry', default=False, help='Do not run, just output command args into output file..')
@click.pass_context
def cli(ctx, dry):
    '''
    Top level command line interface including top level options such as --dry
    '''
    # we explicitly pass --dry to each command (using @click.pass_context) via a click context.
    # see https://click.palletsprojects.com/en/7.x/complex/ for more on context
    ctx.ensure_object(dict) # ensure that ctx.obj exists and is a dict (in case `cli()` is called by means other than in the below if __name__ == '__main__': 
    ctx.obj['DRY'] = dry #set 'DRY' key in the context to the top level option value

@cli.command()
@click.option('--option1')
@click.option('--option2')
@click.option('--option3')
@click.pass_context
def command1(ctx, option1, option2, option3):
    '''
    A command belonging to the top level cli group.
    '''
    click.echo('Dry run is %s' % (ctx.obj['DRY'] and 'on' or 'off'))
    click.echo('command1 run with option1: {}, option2: {}, option3: {}'.format(option1, option2, option3))

if __name__ == '__main__':
    cli(obj={})
