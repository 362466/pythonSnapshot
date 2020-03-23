import boto3
import click

session = boto3.Session(profile_name='python')
ec2 = session.resource('ec2')


@click.command()
@click.option('--project', default=None, help="Only instance for project")
def list_instances(project):
    instances = []
    if project:
        print("in if")
        filters = [{'Name': 'tag:project', 'Values': [project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        print("in else")
        instances = ec2.instances.all()

    for i in instances:
        print(i.id)


if __name__ == "__main__":
    list_instances()