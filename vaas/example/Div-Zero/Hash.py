from DNA.interop.System.Storage import GetContext, Get, Put, Delete
from DNA.interop.System.Runtime import CheckWitness, GetTime, Notify, Serialize, Deserialize, Log
from DNA.interop.System.ExecutionEngine import GetExecutingScriptHash
from DNA.interop.System.Blockchain import GetHeight, GetHeader, GetBlock
from DNA.interop.System.Header import *
from DNA.interop.DNA.Native import Invoke
from DNA.builtins import *
from DNA.interop.System.App import DynamicAppCall
from DNA.interop.DNA.Contract import Migrate
from DNA.interop.DNA.Runtime import GetCurrentBlockHash
############################################core start #################################################
def Main(opration, args):
    if opration == "hash":
        time = GetTime()
        height = GetHeight()
        header = GetHeader(height)
        a = args[0] / abs(GetBlockHash(header)) 
        a = a / abs(time)
        now_hash = GetBlockHash(header)
        a = a % abs(now_hash)
        return a
    return False
