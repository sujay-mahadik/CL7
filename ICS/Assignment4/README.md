# Vulnerability assessment tools
Configure and demonstrate use of vulnerability assessment tool such as Snort tool for intrusion or SSL Web security.

## Workflow for analysing a .pcap file

- Download and install Wireshark
- Use Wireshark for capturing packets and making a .pcap file
- Download and install Snort
- Use Snort CLI to analyze the .pcap file

## Wireshark

Wireshark is a free and open source packet analyzer. It is used for network troubleshooting, analysis, software and communications protocol development, and education.[ref](https://en.wikipedia.org/wiki/Wireshark)

### Installation and Packet Capturing

- Download the setup from [here](https://www.wireshark.org/#download)
- Follow the [documentation](https://www.wireshark.org/docs/wsug_html/)
- Capture packet data into [.pcap files](https://www.wireshark.org/docs/wsug_html/#ChCapCaptureFiles)

## Snort
Snort is an open source network intrusion prevention system, capable of performing real-time traffic analysis and packet logging on IP networks. It can perform protocol analysis, content searching/matching, and can be used to detect a variety of attacks and probes, such as buffer overflows, stealth port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more. [ref](https://www.snort.org/faq/what-is-snort)

### Installation and Packet Analysing

- Download the setup from [here](https://www.snort.org/downloads#snort-downloads) and install snort
- Follow the [documentation](https://snort-org-site.s3.amazonaws.com/production/release_files/files/000/008/467/original/snort_manual.html?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIXACIED2SPMSC7GA%2F20180922%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180922T074600Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=26249b1e5913bafb8dccf31878534142e94d67fbdc913b692e9174c96cf7b036#_first_steps)
- Examine the .pcap file created using wireshark

> snort -r a.pcap

## Further reading and more tools
[Open Source for u](https://opensourceforu.com/2012/02/top-10-security-assessment-tools/)

[Hacker Target](https://hackertarget.com/10-open-source-security-tools/)