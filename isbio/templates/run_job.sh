#!/bin/bash
# Automagically generated by Breeze ( $url )
# Generated $date ($tz)
# Generated by $user
# Target is $target

# Non language specific, non target specific, job bootstrap file
# Clem 06/05/2016
# compatible with :
# 	compute targets : sge, docker
# 	language 	: R (possibly others)
# Configuration variables, parsed and filled from Breeze
FAILED_FN=$failed_fn
INCOMPLETE_FN=$inc_run_fn
SUCCESS_FN=$success_fn
DONE_FN=$done_fn
IN=$file_name
OUT=$out_file_name
EXEC_PATH=$full_path
EXEC_ARGS="$args"
EXEC_CMD="$cmd"
RUN_LINE="$EXEC_PATH $EXEC_CMD"
FAILED_TEXT="$failed_txt"
POKE_URL="$poke_url"
TARGET="$target"
## END OF CONFIGURATION
ARCH=$arch_cmd
VERSION=$version_cmd
OS=`cat /etc/system-release`
KERNEL=`uname -mrs`
echo 'host    : '`hostname`' @ '`hostname -i`
echo 'os      : '$OS
echo 'kernel  : '$KERNEL
echo 'arch    : '$ARCH
echo 'dir     : '`pwd`
echo 'target  : '$TARGET
echo 'exec    : '$RUN_LINE
echo 'version : '$VERSION"\n"
# removing possibly existing files generated from a previous run
rm *~ $OUT $FAILED_FN $INCOMPLETE_FN $SUCCESS_FN $DONE_FN > /dev/null 2>&1
wget -qO- $POKE_URL'starting' > /dev/null
echo `date`
echo -n 'Running '$IN'...'
# Running the job
touch ./$INCOMPLETE_FN && `$RUN_LINE`
CODE=$?
echo ' done !'
if [ $CODE -eq 0 ]; 
then
	touch ./$SUCCESS_FN
fi
echo `date`
# Removes incomplete run file flag
rm ./$INCOMPLETE_FN > /dev/null 2>&1
CMD=`tail -n1<./$OUT`
# check the last line of the Rout file for possible job internal failure
if [ "$CMD" = "$FAILED_TEXT" ] || [ ! -f "$DONE_FN" ]; 
then
	touch ./$FAILED_FN
	cat $OUT
	echo 'Failure !'
	wget -qO- $POKE_URL'failed/'$CODE > /dev/null
	exit $CODE
else
	wget -qO- $POKE_URL'success' > /dev/null
	echo 'Success !'
fi
# removes any possible temp file (we don't want them to be part of the resulting folder)
rm *~ > /dev/null 2>&1
exit 0
