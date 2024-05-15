 with a public subnet and a private subnet.

I have tried to use the following code:


from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.aws.network import VPC
from diagrams.aws.network import InternetGateway
from diagrams.aws.network import NATGateway
from diagrams.aws.network import VPCGatewayAttachment
from diagrams.aws.network import VPCSubnet
from diagrams.aws.network import VPCSubnetRouteTable
from diagrams.aws.network import VPCSubnetRouteTableAssociation
from diagrams.aws.network import VPCSubnetRouteTablePropagation
from diagrams.aws.network import VPCSubnetNetworkAcl
from diagrams.aws.network import VPCSubnetNetworkAclAssociation
from diagrams.aws.network import VPCSubnetNetworkAclEntry
from diagrams.aws.network import VPCSubnetNetworkAclEntryRule
from diagrams.aws.network import VPCSubnetNetworkAclEntryRuleEgress
from diagrams.aws.network import VPCSubnetNetworkAclEntryRuleIngress
from diagrams.aws.network import VPCSubnetNetworkAclEntryRuleEgressRule
from diagrams.aws.network import VPCSubnetNetworkAclEntryRuleIngressRule
from diagrams.aws.network import VPCSubnetNetworkAclEntryRuleEgressRuleAction
from diagrams.aws.network import VPCSubnetNetworkAclEntryRuleIngressRuleAction
from diagrams.aws.network import VPCSubnetNetworkAclEntryRuleEgressRuleCidr
from diagrams.aws.network import VPCSubnetNetworkAclEntryRuleIngressRuleCidr
from diagrams.aws.network import VPCSubnetNetworkAclEntryRuleEgressRulePort
from diagrams.aws.network import VPCSubnetNetworkAclEntryRuleIngressRulePort
from diagrams.aws.network import VPCSubnetNetworkAclEntryRuleEgressRuleProtocol
from diagrams.aws.network import VPCSubnetNetworkAclEntryRuleIngressRuleProtocol
from diagrams.aws.network import VPCSubnetNetworkAclEntryRuleEgressRuleSource
from diagrams.aws.network import VPCSubnetNetworkAclEntryRuleIngressRuleSource
from diagrams.aws.network import VPCSubnetNetworkAclEntryRuleEgressRuleSourceCidr
from diagrams.aws.network import