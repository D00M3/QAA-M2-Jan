import logging 
import os
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
# exit(main())

log = logging.getLogger("new-logger")
log2 = logging.getLogger("other logger")
log.info("Hello World")
log.debug("Hello all")
log.info("new thing")

log2.critical("AHHHH DANGER")