import click
from utils import to_list
from utils import _to_list
from utils import _zip_data
from utils import _unzip_data
from utils import output_txt

def zip_data(Ifile_name, Ofile_name):
    rsid, alleles = to_list(Ifile_name)
    zip_datas = _zip_data(rsid, alleles)
    output_txt(zip_datas, Ofile_name)


def unzip_data(Ifile_name, Ofile_name):
    rsid, alleles = _to_list(Ifile_name)
    unzip_datas = _unzip_data(rsid, alleles)
    output_txt(unzip_datas, Ofile_name)

@click.group()
def cli():
    pass


@cli.command()
@click.option('--choice', prompt='请输入指令（zip为压缩，unzip为解压）:',
              type=click.Choice(['zip', 'unzip']),help='zip为压缩，unzip为解压')

@click.option('--ifile_name', prompt='请输入待压缩文件路径名称：', default='',
              help='仅支持23andme, Wegene和23魔方')

@click.option('--Ofile_name', prompt='请输入输出压缩文件路径名称：', default='')

def start(choice, ifile_name, ofile_name):
    if choice == 'zip':
        zip_data(ifile_name, ofile_name)
        click.echo(click.style('压缩完成',fg='green'))
    elif choice == 'unzip':
        unzip_data(ifile_name, ofile_name)
        click.echo(click.style('解压完成',fg='green'))
    else:
        click.echo(click.style('没有此命令，请输入zip或unzip',fg='red'))


if __name__ == '__main__':
    cli()